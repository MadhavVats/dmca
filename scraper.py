from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time



DRIVER_PATH = '/Users/madhavvats/Downloads/chrome-mac-arm64'
driver = webdriver.Chrome()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
}

def is_match(title:str, names: list[str]) -> bool:
    title = title.lower()
    for name in names:
        name = name.lower()
        if name in title:
            return True
        if not ' ' in names:
            continue
        splits = name.split(' ')
        for split in splits:
            if split not in title:
                return False
        return True
    return False

def recur_image_urls(names, copyrights, depth):
    if depth == 0:
        return
    # title = driver.find_element(By.XPATH, "//h1").text
    # anchors = driver.find_elements(By.XPATH, ".//a[@href]")
    # source_url = anchors[0].get_attribute("href")
    # if is_match(title, names):
    #     copyrights.append((title, source_url))
    related_divs = driver.find_element(By.XPATH, "//div[@role='dialog']").find_elements(By.XPATH, "//div[@data-ri]")
    for cnt in range(len(related_divs[:2])):
        div = driver.find_elements(By.XPATH, "//div[@data-ri]")[cnt]
        div.click()
        time.sleep(1)
        recur_image_urls(names, copyrights, depth-1)
        driver.back()
        time.sleep(1)

def fetch_image_urls(query, names: list[str]):
    search_url = "https://www.google.com/search?hl=en&tbm=isch&q=" + query
    driver.get(search_url)
    divs = driver.find_elements(By.XPATH, "//div[@data-attrid='images universal']")
    copyrights = []
    for cnt in range(len(divs[:2])):
        print(len(driver.find_elements(By.XPATH, "//div[@data-attrid='images universal']")))
        div = driver.find_elements(By.XPATH, "//div[@data-attrid='images universal']")[cnt]
        div.click()
        time.sleep(1)
        recur_image_urls(names, copyrights, 2)
        driver.back()
        time.sleep(1)

    print(copyrights)
    driver.quit()


fetch_image_urls("abc", ["abc"])
