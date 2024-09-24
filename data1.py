import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = []

    # Example of extracting item data (depends on website structure)
    for item in soup.find_all('div', class_='item-class'):
        title = item.find('h2').text
        price = item.find('span', class_='price-class').text
        link = item.find('a')['href']
        items.append({'title': title, 'price': price, 'link': link})

    return items

# URLs of the websites to scrape
urls = [
    'https://oldnavy.gapcanada.ca/browse/category.do?cid=1031099&nav=hamnav%3AMen%3AShop%20Men%E2%80%99s%20Categories%3AShop%20All%20Men%27s#department=75',
    'https://www.gapcanada.ca/browse/category.do?cid=1127944#pageId=0&department=75&mlink=5058,HP_Promo_Main_M',
    #'https://website3.com/clothing'
]

all_items = []
for url in urls:
    all_items.extend(scrape_website(url))

# Save the scraped data or use it as needed
print(all_items)

