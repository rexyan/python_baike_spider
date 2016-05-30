#-*-coding:utf-8 -*-
#---------------------------------------
#   程序：根据明星关系抓取明星百科页面
#   版本：1.0
#   作者：rexyan
#   日期：2016-5-30
#   语言：Python 3
#   操作：输入任何明星百科页面，作为起点
#   功能：目前实现跨页面抓取明星页面，后期可绘制关系图（给我一个明星，还你一个娱乐圈）
#	示例：
#		  ——>王力宏
#		  		——>妻子:李靓蕾
#						——>....
#		  				——>....
#		  		——>女儿:王嘉莉
#		  		——>弟弟:王力德
#		  		——>好友:萧亚轩
#		  				——>前男友:柯震东
#		  						——>....
#		  						——>....
#		  				——>前男友:王阳明
#		  						——>....
#		  						——>....
#		  				——>好友:王力宏
#
#
#---------------------------------------

from urllib.request import urlopen
from bs4 import  BeautifulSoup
import re
import random
import datetime

random.seed(datetime.datetime.now())
urllist=set()
def func1(zurl):
    url=zurl
    request=urlopen(url)
    result=BeautifulSoup(request)
    return result

def matching(newurl):
    s=(newurl.findAll('a',href=re.compile('^(http:\/\/baike\.baidu\.com\/item\/)')))
    return s


baike=input('please input baike:')
def main():
    global baike
    return_func1=func1(baike)
    return_matching=matching(return_func1)
    print (return_func1.find('h1').get_text())
    for x in return_matching:
        if 'href' in x.attrs:
            url = (x.attrs['href'])
            if url not in urllist:
                print('我们发现了新的页面，正在记录它')
                print(url)
                urllist.add(url)
                print('记录完成，爬虫正在爬取它的信息')
                baike=url
                main()
                
if __name__=='__main__':
    main()
    print(urllist)




