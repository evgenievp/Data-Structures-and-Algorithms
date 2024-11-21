import requests
import bs4

url = 'https://jsonplaceholder.typicode.com'

web_site = requests.get(url)
web_content = web_site.text
soup = bs4.BeautifulSoup(web_content, 'html.parser')

sections = soup.find_all('h2')
titles = []
for tag in sections:
    titles.append(tag.text)
for title in titles:
    print(title)
