import requests
import re

headers={
     'User-Agent':'spider',
     'Cookie': 'SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WFRD2zQV.Nv5liSuzVQRIme; SINAGLOBAL=1619748558311.7532.1648224332278; _ga=GA1.2.1761206650.1648261853; UOR=www.google.com.hk,weibo.com,www.reddit.com; SUB=_2AkMVEyk6f8NxqwJRmP4Qz2PnaI9wzwnEieKjT9jhJRMxHRl-yT9jqmwJtRB6PpMHyJrCQfUp96jttrVFyWTXCJncWkeb; XSRF-TOKEN=4f8RUht1K3EMZh6KtX_iOJCp; _s_tentry=weibo.com; Apache=8663029303723.884.1651209220471; ULV=1651209220502:5:4:2:8663029303723.884.1651209220471:1650632005852; WBPSESS=kErNolfXeoisUDB3d9TFH7v_0508OYh5kSAiPW__Ihin_d28-zMtt78hVQtGMPB0afmMk9jmuXbmGvF2evmwBO-DdU8Bgc4Vxrzej-h8yLr9q39ggvUNBtj-pkMhxRy-V2FfV17SoQQ3jrsumSdwKNvrKzT_gSeapK7RPdKBXo8=; PC_TOKEN=0dee64ed41'
}
r=requests.get('https://s.weibo.com/top/summary',headers=headers).text
pattern=re.compile(r'target="_blank">(.*?)</a>',re.S)
titles=re.findall(pattern,r)
print(titles)

with open('weibo.txt','w') as f:
    for i in range(len(titles)-2):
        f.write(titles[i])
        f.write('\n')