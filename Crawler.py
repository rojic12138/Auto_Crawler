import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import os

headers={
     'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
}
r=requests.get('http://jhsjk.people.cn/',headers=headers).text
    
pattern1=re.compile(r'<li><a href="article/(.*?)\?isindex=1" target="_blank"><span>.*?</span><i>.*?</i></a></li>')
ids=re.findall(pattern1,r)
pattern2=re.compile('<li><a href="article/.*?\?isindex=1" target="_blank"><span>(.*?)</span><i>.*?</i></a></li>')
titles=re.findall(pattern2,r)

flag=False
with open('info.txt','r',encoding='utf-8') as f:
    title=f.readline().strip()
    print(title)
    print(titles[0])
    if(title!=titles[0]):
        #更新
        flag=True
        
def Get_article(article_id):
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get('http://jhsjk.people.cn/article/'+article_id)
    
    title=browser.find_element(By.XPATH,'/html/body/div[5]/h1').text
    info=browser.find_element(By.XPATH,'/html/body/div[5]/div[1]').text
    paras=browser.find_elements(By.XPATH,'/html/body/div[5]/div[2]/p')
    with open('article.txt','w',encoding='utf-8') as f:
        f.write(title)
        f.write('\n')
        f.write('\n')
        f.write(info)
        f.write('\n')
        for para in paras:
            f.write(para.text)
            f.write('\n')
   
#print(flag)
if(flag):
    with open('info.txt','w',encoding='utf-8') as f:
        f.write(titles[0])
        f.write('\n')
        f.write(ids[0])
    Get_article(ids[0])
    
env_file = os.getenv('GITHUB_ENV')
with open(env_file, "a") as myfile:
    myfile.write("CHANGED="+str(flag))
