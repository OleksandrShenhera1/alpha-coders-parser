from PyQt6.QtCore import QObject, pyqtSignal

from playwright.sync_api import sync_playwright
import os
import requests
import subprocess
from pathlib import Path

class ParserWorker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    log_message = pyqtSignal(str)

    def __init__(self, best, latest, popular, pg_count, output_dir):
        super().__init__()
        self.best = best
        self.latest = latest
        self.popular = popular
        self.pg_count = pg_count
        self.output_dir = output_dir
        self.is_running = True

    
    def run(self):
        self.total_steps = 0
        if self.best:
            self.total_steps += self.pg_count * 12
        if self.latest:
            self.total_steps += self.pg_count * 12
        if self.popular:
            self.total_steps += self.pg_count * 12
        self.current_step = 0

        if self.best:
            self.best_parse()
        if self.latest:
            self.latest_parse()
        if self.popular:
            self.popular_parse()
        self.finished.emit()


    def best_parse(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            pages: int = self.pg_count
            output_path = Path(self.output_dir) / "best_img"
            output_path.mkdir(parents=True, exist_ok=True)

            img_counter = 0

            for j in range(1, pages + 1):
                
                if not self.is_running:
                    break

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
                                with open(output_path / f"img_best_{img_counter}.jpg", "wb") as f:
                                    f.write(response.content)
                                    self.log_message.emit(f"img_best_{img_counter} Status: saved.")
                                    img_counter += 1
                                    self.current_step += 1
                                    progress_value = int((self.current_step / self.total_steps) * 100)
                                    self.progress.emit(progress_value)
                            else:
                                self.log_message.emit(f"img_best_{img_counter} Failed while saving.")
                                img_counter +=1
                        except Exception as e:
                            self.log_message.emit(f"(Error) url: {img_url} => {e}.")
                    
    
    def latest_parse(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            pages: int = self.pg_count
            output_path = Path(self.output_dir) / "latest_img"
            output_path.mkdir(parents=True, exist_ok=True)

            img_counter = 0

            for j in range(1, pages + 1):
                
                if not self.is_running:
                    break

                if j == 1:
                    url = "https://alphacoders.com/newest"
                else:
                    url = (f"https://alphacoders.com/newest?page={j}")
                
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
                                with open(output_path / f"img_latest_{img_counter}.jpg", "wb") as f:
                                    f.write(response.content)
                                    self.log_message.emit(f"img_latest_{img_counter} Status: saved.")
                                    img_counter += 1
                                    self.current_step += 1
                                    progress_value = int((self.current_step / self.total_steps) * 100)
                                    self.progress.emit(progress_value)
                            else:
                                self.log_message.emit(f"img_latest_{img_counter} Failed while saving.")
                                img_counter +=1
                        except Exception as e:
                            self.log_message.emit(f"(Error) url: {img_url} => {e}.")

    def popular_parse(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            pages: int = self.pg_count
            output_path = Path(self.output_dir) / "popular_img"
            output_path.mkdir(parents=True, exist_ok=True)

            img_counter = 0

            for j in range(1, pages + 1):
                
                if not self.is_running:
                    break

                if j == 1:
                    url = "https://alphacoders.com/popular"
                else:
                    url = (f"https://alphacoders.com/popular?page={j}")
                
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
                                with open(output_path / f"img_popular_{img_counter}.jpg", "wb") as f:
                                    f.write(response.content)
                                    self.log_message.emit(f"img_popular_{img_counter} Status: saved.")
                                    img_counter += 1
                                    self.current_step += 1
                                    progress_value = int((self.current_step / self.total_steps) * 100)
                                    self.progress.emit(progress_value)
                            else:
                                self.log_message.emit(f"img_popular_{img_counter} Failed while saving.")
                                img_counter +=1
                        except Exception as e:
                            self.log_message.emit(f"(Error) url: {img_url} => {e}.")


    def stop(self):
        self.is_running = False




        
