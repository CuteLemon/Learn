import requests
import json

from lxml import html
# get url from newsapi
API_KEY = '88a2ee685e47485a94999d98bbe49beb'
SOURCE = 'cnn'

def getNews():
	url = 'https://newsapi.org/v1/articles?source=' + SOURCE + \
	 		'&sortBy=top&apiKey=' + API_KEY
	response = requests.get(url)
	json_content = json.loads(response.content)
	print json_content
	if (json_content['status']== 'ok'):
		for news in json_content['articles']:
			print news['title']
			print '----------'
		return list(json_content['articles'])
	else:
		return None

CNN_XPATH = '''//p[@class="zn-body__paragraph"]//text() | //div[@class="zn-body__paragraph"]//text()'''
TEST_URL = 'http://edition.cnn.com/2017/07/06/us/georgia-stabbings-gwinnett-county/index.html'

def scraperNews(articles):
	response = requests.get(TEST_URL)
	tree = html.fromstring(response.content)
	news = tree.xpath(CNN_XPATH)
	news = ''.join(news)
	print news

if __name__ == '__main__':
	print 'test begin:...'
	news_urls = getNews()
	scraperNews(news_urls)
