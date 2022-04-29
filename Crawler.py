import requests
import re

headers={
     'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
}
r=requests.get('http://jhsjk.people.cn/',headers=headers).text
    
pattern1=re.compile(r'<li><a href="article/(.*?)\?isindex=1" target="_blank"><span>.*?</span><i>.*?</i></a></li>')
ids=re.findall(pattern1,r)
#print(ids)
pattern2=re.compile('<li><a href="article/.*?\?isindex=1" target="_blank"><span>(.*?)</span><i>.*?</i></a></li>')
titles=re.findall(pattern2,r)
#print(titles)

flag=False
with open('article.txt','r') as f:
    title=f.read()
    if(title!=titles[0]):
        #更新
        flag=True
        
def Get_article(article_id):
    r=requests.get('http://jhsjk.people.cn/article/'+article_id,headers=headers).text
    title=re.findall('<h1>(.*?)</h1>',r)[0]
    infos=re.findall('<div class="d2txt_1 clearfix">(.*?)&nbsp;&nbsp;(.*?)</div>',r)
    paras=re.findall(r'\n<p style="text-indent: 2em;">(.*?)</p>',r,re.DOTALL)
    print(r)
    print(paras)
    with open('article.txt','w') as f:
        f.write(title)
        f.write('\n')
        f.write('\n')
        f.write(infos[0][0])
        f.write(infos[0][1])
        f.write('\n')
        for para in paras:
            f.write(para)
            f.write('\n')
    
if(flag):
    with open('info.txt','w') as f:
        f.write(titles[0])
        f.write('\n')
        f.write(ids[0])
    Get_article(ids[0])