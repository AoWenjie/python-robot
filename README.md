# python-robot
## 第一个项目是爬取小说
主要用到了requests,BeautifulSoup这两个库，以及lxml解析器
### 步骤
0、获取小说目录页面的html  
1、用BeautifulSoup+lxml解析  
2、找出所有章节的链接，拼接链接  
3、进入所有的章节链接，找出章节的文本内容部分，然后写入本地    
### 使用方法
在网站中找到小说对应的那串数字，更换代码中的数字就可以实现下载不同的小说

`req = requests.get('http://www.biquge.com.cn/book/29209/',headers = headers)`

book后面的数字就是书对应的序列号
    
