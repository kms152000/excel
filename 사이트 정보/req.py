import requests
from bs4 import BeautifulSoup

"""
response = requests.get('https://www.naver.com/', verify=False)

print(response.status_code)
print("\n")
print(response.text)
"""

"""
url = 'https://kin.naver.com/search/list.nhn?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'
response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select_one('#s_content > div.section > ul > li:nth-child(2) > dl > dt > a')
    print(title)
    print(title.get_text())
else:
    print(response.status_code)
"""


url = 'https://kin.naver.com/search/list.nhn?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    ul = soup.select_one('ul.basic1')
    titles = ul.select('li > dl > dt > a')
    print(ul)
else : 
    print(response.status_code)