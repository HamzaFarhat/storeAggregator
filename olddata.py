import requests
from bs4 import BeautifulSoup

# URLs to scrape
urls = ['https://bananarepublic.gapcanada.ca/browse/division.do?cid=5343'] #This is only for the 

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract desired information
    title = soup.find('t-shirts').text
    print(f'Title of {url}: {title}')