#python3
import urllib.request
import urllib.parse
from urllib.parse import urlparse
import http.client

import time
import datetime

import json

def http_client(schema,host,port,method,url,body,headers):
    if schema == "HTTP":
        conn = http.client.HTTPConnection(host,port)
    else:
        conn = http.client.HTTPSConnection(host,port)
    if body:
        # if body is string, it will be encoded as ISO-8851-1,not utf-8
        body = body.encode("utf-8")
    conn.request(method,url,body,headers)
    response = conn.getresponse()
    headers = response.getheaders()
    html = response.read().decode('utf-8')
    conn.close()
    return html,headers

def http_index(status):
    schema = "HTTP"
    host = "127.0.0.1"
    port = "9200"
    method = "PUT"
    url = "/sinaweibo_v1/status/"+str(status["id"])
    body = json.dumps(status,ensure_ascii=False,indent=4)
    print(body)
    headers = {}

    html,rheaders = http_client(schema,host,port,method,url,body,headers)
    print(html)
    print(rheaders)

def utc2timestamp(datetime_str):
    return int(datetime.datetime.strptime(datetime_str,"%a %b %d %X %z %Y").timestamp())

if __name__ == '__main__':

    baseURL = "https://api.weibo.com/2/"
    accesstoken = "2.00nMzqcCzSxBND29ae6e2313XYGc5D"
    #
    maxCount = 100
    countPerPage = 100
    maxPages = int(maxCount / countPerPage)
    #
    pausePerReq = 1 #seconds
    #
    url = baseURL+"statuses/public_timeline.json"+"?access_token="+accesstoken+"&count="+str(countPerPage)+"&base_app=0"
    for i in range(maxPages):
        response = urllib.request.urlopen(url)
        res_json = response.read().decode('utf-8')
        json_dic = json.loads(res_json)
        for status in json_dic.get("statuses",{}):
            user = status.get("user")
            user["created_at"] = utc2timestamp(status["created_at"])
            #status.pop("annotations", None)
            #status.pop("darwin_tags",None)
            status["created_at"] = utc2timestamp(status["created_at"])
            http_index(status)
            print("###############")
        time.sleep(pausePerReq)


