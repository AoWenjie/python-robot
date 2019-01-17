import requests
from bs4 import BeautifulSoup

ttt
serverName = 'http://www.biquge.com.cn'
storyUrls = [] #每章小说的URL
storyNames = [] #每章小说的名字
storyNums = 0 #总的章节数

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

req = requests.get('http://www.biquge.com.cn/book/29209/',headers = headers)
req.encoding = 'utf-8'
bs = BeautifulSoup(req.text,'lxml')

#得到小说名字，作者
storyName = bs.find('div',id = 'info')
for i in range(1,len(storyName.text)):
    if(storyName.text[i] == '\n'):
        numOfName = i
        break
dirAndName = (storyName.text)[1:numOfName] + ".txt"
F= open(dirAndName,'a',encoding = 'utf-8')
print("打印小说信息")
print((storyName.text))
F.write((storyName.text) + '\n\n\n')

#得到小说目录的所有地址
_content = bs.find('div',id = 'list')
novel_list = _content.find_all('a')

#获得章节总数
storyNums = len(novel_list)

for a in novel_list:
    #保存每个章节的URL
    storyUrls.append(serverName + a.get('href'))
    #保存每章的名字
    storyNames.append(a.string)
    #print(a.string,serverName + a.get('href'))


for i in range(storyNums):
    req1 = requests.get(storyUrls[i])
    req1.encoding = 'utf-8'
    bs1 = BeautifulSoup(req1.text,'lxml')
    texts = bs1.find('div',id = 'content')
    print('当前正在写入' + str(i + 1) +'章：' + storyNames[i])
    F.write(storyNames[i] + "\n")
    F.write(texts.get_text("\n\n","<br/>"))
    F.write('\n\n\n\n')