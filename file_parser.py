from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from pathlib import Path
import warnings
import logging
import requests
import time
# Ignore python waringings
warnings.filterwarnings("ignore")

# Ignore selenium warnings (only selenium v.4+)
logging.getLogger('selenium').setLevel(logging.CRITICAL)

options = Options()

# Turn off chrome driver warnings (chromedriver)
options.add_experimental_option('excludeSwitches', ['enable-logging'])

options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=options)

print("Enter Count Of Pages To Download: ", end='')
countOfPages = int(input())


baseLink = "https://alphacoders.com/the-best-wallpapers?month=all&year=all"

imgIndex = 0
errorCount = 0
for page in range(1, countOfPages + 1):
    
    if page==1:
    
        link = baseLink
    else:
         link = f"{baseLink}&page={page}"

    driver.get(link)
    
    time.sleep(2)
    
    blocks = driver.find_elements(By.CLASS_NAME, "item")
    
    # Create folder to save images
    Path("images").mkdir(parents=True, exist_ok=True)

    for block in blocks:
        try:
             
            # Find url
            meta = block.find_element(By.CSS_SELECTOR, 'meta[itemprop="contentUrl"]')
            imgUrl = meta.get_attribute("content")
            print(imgIndex, ": ", end='')
            print(imgUrl)
            # Download photo
            response = requests.get(imgUrl)
            if response.status_code == 200:
                with open(f"images/img_{imgIndex}.jpg", "wb") as f:
                        f.write(response.content)
            imgIndex += 1

        except Exception as e:
             print(f"Error: {e}")
             errorCount += 1

if errorCount == 0:
     print("All images downloaded successfully!", end='')
else:
     print(f"{errorCount} error(s) occurred while downloading files", end='')
     
driver.close()
