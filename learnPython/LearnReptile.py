import urllib3
import re
import requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def getHtml(url):
    http = urllib3.PoolManager();
    # 打开网页
    page = http.request('GET','http://tieba.baidu.com/p/1753935195');
    #读取页面源码
    htmlcode = page.data;
    return htmlcode;
    # print(htmlcode);

reg = b'src="(.+?\.jpg)" width'; #正则表达式
reg_img = re.compile(reg);   #编译一下，运行更快
# print( reg_img.findall(getHtml("http://tieba.baidu.com/p/1753935195")))
text = getHtml("http://tieba.baidu.com/p/1753935195");
print(text)
imglist = reg_img.findall(text);   #进行匹配
for img in imglist:
    print(img)
