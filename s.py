import bs4 as bs
import urllib.request
import csv

source = urllib.request.urlopen('http://books.toscrape.com/').read()

soup = bs.BeautifulSoup(source,'lxml')
#article = soup.find('article',class_= 'product_pod')

for article in soup.find_all('article'):
	src = article.find('img',class_='thumbnail').get('src')
	title = print(article.find('h3').get_text()
	ratings = article.find('p').get('class')[1]
	price = article.find('p',class_='price_color').get_text()
	stock_availability = article.find('p',class_='instock availability').get_text()


with open('task.csv', 'w') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Image Source'] + ['Title'] + ['Ratings'] + ['Price'] + ['Availability'])
    spamwriter.writerow(['src', 'title', 'ratings','price','stock_availability'])
