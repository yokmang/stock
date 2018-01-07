#!/usr/local/bin/python3
#naver에서 가져와보자...

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs
import pandas as pd
import re

def get_fs_naver(ticker,item):
    fs_url = "http://finance.naver.com/item/main.nhn?code="+ticker
    req = Request(fs_url)
    html_text = urlopen(req).read()

    soup = bs(html_text, 'lxml')
    d = soup.find(text=item)
    d_ = d.find_all_next(class_="")

    data = d_[0:3]
    res = [float(v.text) for v in data]

    return(res)

def get_profile_naver(ticker):
    fs_url = "http://finance.naver.com/item/main.nhn?code="+ticker
    req = Request(fs_url)
    html_text = urlopen(req).read()
    
    soup = bs(html_text, 'lxml')
    t = soup.find(text="종목 시세 정보")
    t_ = t.find_all_next("dd")

    title = []
    #종목 이름
    title.append(t_[1].text[3:].strip())
    #종목코드
    title.append(ticker)

    ror = re.search('(\d+)(\s\w+)', t_[3].text[3:].replace(',',''))
    #현재 주가
    title.append(float(ror[1]))

    number  = soup.find(text="상장주식수")
    number_ = float(number.find_next("td").text.replace(',',''))
    #주식수
    title.append(number_)

    d = soup.find(text="당좌비율")
    d_ = d.find_all_next(class_="")

    data = d_[2]
    title.append(float(data.text))

    bd = soup.find(text="주당배당금(원)")
    bd_ = bd.find_all_next(class_="")

    data = bd_[2]
    title.append(float(data.text))

    return title

#print (get_profile_naver("002460"))
#print (get_fs_naver("002460","당좌비율") )
#print (get_fs_naver("002460","주당배당금") )


"""
fs_url = "http://finance.naver.com/item/main.nhn?code=002460"
df = pd.read_html(fs_url)
req = Request(fs_url)
html_text = urlopen(req).read()

soup = bs(html_text,'html.parser')
                  
item = "당좌비율"
#print(soup)
d  = soup.find(text=item)
print(d)
#부채비율 당좌비율 유보율만 찾아지고 나머지는 안찾아짐
#무엇이 문제인지 모르겠다.
d_ = d.find_all_next("td",class_="")

data = d_[0:3]
res = [float(v.text) for v in data]
print (res)
"""

