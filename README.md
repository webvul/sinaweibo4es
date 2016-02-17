# sinaweibo4es
一个新浪微博采集器, 只有一个python 3 文件，利用新浪微博的public timeline api 抓取实时的微博然后利用http导入到elastic search. 
 
    中文分词采用我的git仓库中的一个ecjk分词插件，需要将其拷贝到es的plugin文件夹里。
    创建es索引sinaweibo_v1,使用文件sinaweibo_v1.json 文件。将创建一个status mapping。
    最后，运行python3 weibospider.py 即可，你可根据需要修改py文件中的http，port，采集微博数量等。
