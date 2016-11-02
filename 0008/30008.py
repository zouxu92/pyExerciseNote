import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
    'Host': "www.yinwang.org",
    'Pragma': "no-cache"	
}

requests = requests.Session()

def get_doc_urls():
	result = {}
	req = requests.get("http://blog.csdn.net/huangxiongbiao/article/details/45557631", headers=headers, verify=False)
	soup = BeautifulSoup(req.content, "lxml")
	tmp = soup.find_all('li', class_="list-group-intem title")
	for block in tmp:
		title = block.a.text
		url = block.a.get("href")
		result[title] = url
	return result

if __name__ == "__main__":
	print (get_doc_urls())