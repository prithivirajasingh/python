import requests
import bs4

base_url = 'https://quotes.toscrape.com/page/{}/'
page_num = 0
all_authors = set()
all_quotes = []
tags = []
while True:
    page_num += 1
    req = requests.get(base_url.format(page_num))
    # print(req.text)
    soup = bs4.BeautifulSoup(req.text, 'lxml')

    if page_num == 1:
        for items in soup.select('.tag-item'):
            tags.append(items.text.replace('\n',''))

    for index,items in enumerate(soup.select('.text')):
        all_quotes.append(items.text)

    for index,items in enumerate(soup.select('.author')):
        # print(authors[index].text)
        all_authors.add(items.text)

    if soup.select('.author') == [] or page_num == 15:
        break

print(tags)
print('')
print(all_quotes)
print('')
print(all_authors)
