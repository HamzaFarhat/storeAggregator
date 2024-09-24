from selenium import webdriver # type: ignore
from selenium.webdriver.chrome.options import Options # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore
from selenium.webdriver.common.action_chains import ActionChains # type: ignore
import time
import requests

################## API CALL ###################

API_KEY = '<YOUR_API_KEY>' # Replace <YOUR_API_KEY> with your API key
url_to_scrape = "https://en.wikipedia.org/wiki/Alexander_the_Great" # Here put the url that you want to scrape

def start_olostep(url):
    querystring = {
        "url_to_scrape": url_to_scrape,
       # optional parameters.
       # If you want to change them, uncomment and see the available options at:
       # https://docs.olostep.com/api-reference/start-agent

       # "timeout": 40,
       # "waitBeforeScraping": 1,
       # "expandMarkdown": True,
       # "expandHtml": False,
       # "saveHtml": True,
       # "saveMarkdown": True,
       # "removeImages": True,
       # "fastLane": False,
       # "removeCSSselectors": 'default',
       # "htmlTransformer": 'none'
    }

    headers = {"Authorization": "Bearer " + API_KEY}

    print("Starting Olostep...")
    response = requests.request(
                    "GET",
                    "https://agent.olostep.com/olostep-p2p-incomingAPI", # API endpoint
                    headers=headers,
                    params=querystring
                )
    print(response.text)
    # response is an object that has the following structure
    # {
    #    "defaultDatasetId": "defaultDatasetId_mngjljq1qc",
    #    "html_content": "",
    #    "markdown_content": " Alexander the Great - Wikipedia...",
    #    "text_content": "",
    #    "usedProvidedNodeCountry": True
    #   }

start_olostep(url_to_scrape)

################ API CALL ENDS #################
# def setup_driver(): # we'll need to modify this according to olostep configs.
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--window-size=1920,1080")
#     driver = webdriver.Chrome(options=chrome_options)
#     return driver

# def scroll_to_bottom(driver):
#     last_height = driver.execute_script("return document.body.scrollHeight")
#     while True:
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(2)
#         new_height = driver.execute_script("return document.body.scrollHeight")
#         if new_height == last_height:
#             break
#         last_height = new_height

# def extract_product_info(driver, url):
#     driver.get(url)
    
#     products = []
    
#     # product grid loader here 
#     WebDriverWait(driver, 30).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, ".category-page-ywl7lp"))
#     )
    
#     scroll_to_bottom(driver)
    
#     # product detail loader(title, price, image)
#     product_elements = driver.find_elements(By.CSS_SELECTOR, ".product-card")
    
#     for product in product_elements:
#         ActionChains(driver).move_to_element(product).perform()
#         try:
#             title = product.find_element(By.CSS_SELECTOR, ".css-0").text
#             price = product.find_element(By.CSS_SELECTOR, ".category-page-r5pe2u").text
#             image = product.find_element(By.CSS_SELECTOR, ".css-1fe0xra").get_attribute("src")
            
#             products.append({
#                 "title": title,
#                 "price": price,
#                 "image": image,
#             })
#         except Exception as e:
#             print(f"Error extracting product info: {e}")
    
#     return products

# def navigate_pages(driver, base_url, max_pages=3):
#     all_products = []
    
#     for page in range(1, max_pages + 1):
#         url = f"{base_url}&page={page}"
#         print(f"Scraping page {page}...")
#         products = extract_product_info(driver, url)
#         all_products.extend(products)
#         print(f"Products found on page {page}: {len(products)}")
#         time.sleep(5)  # waiting for 5 seconds to emulate human behaviour
    
#     return all_products

# def main():
#     base_url = "https://www.gapcanada.ca/browse/category.do?cid=1127944#pageId=0&department=75&mlink=5058,HP_Promo_Main_M"
#     driver = setup_driver()
    
#     try:
#         all_products = navigate_pages(driver, base_url)
        
#         # Print or process the extracted data
#         for product in all_products:
#             print(f"Title: {product['title']}")
#             print(f"Price: {product['price']}")
#             print(f"Image SRC: {product['image']}")
#             print("---")
        
#         print(f"Total Products Extracted: {len(all_products)}")
    
#     finally:
#         driver.quit()

# if __name__ == "__main__":
#     main()