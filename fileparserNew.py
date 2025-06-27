from playwright.sync_api import sync_playwright

import os
import requests
from pathlib import Path

def download_img(best: bool, latest: bool, popular: bool):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        print("Enter page count: ", end='')
        user = int(input())
        pages: int = user
        Path("images").mkdir(parents=True, exist_ok=True)
        img_counter = 0
        for j in range(1, pages + 1):

            if j == 1:
                url = "https://alphacoders.com/the-best-wallpapers?month=all&year=all"
  
            else:
                url = (f"https://alphacoders.com/the-best-wallpapers?month=all&year=all&page={j}")
            
            page.goto(url)
            metas = page.locator('meta[itemprop="contentUrl"]')
            count = metas.count()
            for i in range(count):
                img_url = metas.nth(i).get_attribute('content')
                #print(f"({img_url})", end='')
                if img_url:
                    try:

                        response = requests.get(img_url)
                        if response.status_code == 200:
                            with open(f"images/img_{img_counter}.jpg", "wb") as f:
                                f.write(response.content)
                            print(f"img_{img_counter} Status: saved.")
                            img_counter += 1
                        else:
                            print(f"img_{img_counter} Failed while saving.")
                            img_counter +=1
                    except Exception as e:
                        print(f"(Error) url: {img_url} => {e}.")


download_img()