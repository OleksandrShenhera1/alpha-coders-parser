from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests
import time

options = Options()

options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=options)

link = "https://alphacoders.com/the-best-wallpapers?month=all&year=all"

driver.get(link)

blocks = driver.find_elements(By.CLASS_NAME, "item")

time.sleep(2)

for i, block in enumerate(blocks):
    # Find url
    meta = block.find_element(By.CSS_SELECTOR, 'meta[itemprop="contentUrl"]')
    imgUrl = meta.get_attribute("content")
    print(imgUrl)
    # Download photo
    response = requests.get(imgUrl)
    if response.status_code == 200:
        with open(f"img_{i}.jpg", "wb") as f:
                f.write(response.content)


driver.close()
