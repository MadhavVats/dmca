import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from io import BytesIO
import requests

# Set up Selenium
driver = webdriver.Chrome()

# Function to scroll to the bottom of the page
def scroll_to_bottom():
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


# Open Google Images
search_query = "sunsets"  # Example search term
driver.get(f"https://www.google.com/imghp?hl=en")
time.sleep(2)

# Search for images
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys(search_query)
search_box.send_keys(Keys.RETURN)
time.sleep(2)

# Scroll to the bottom of the page to load more images
scroll_to_bottom()

# Find and click on images to view related images
images = driver.find_elements(By.CSS_SELECTOR, "img.rg_i.Q4LuWd")
print(f"Found {len(images)} images")

output_folder = "downloaded_images"
os.makedirs(output_folder, exist_ok=True)

for index, image in enumerate(images):
    try:
        image.click()
        time.sleep(2)
        
        # Scrape the related images
        related_images = driver.find_elements(By.CSS_SELECTOR, "img.n3VNCb")
        for i, related_img in enumerate(related_images):
            img_url = related_img.get_attribute("src")
            if img_url and 'http' in img_url:
                img_name = f"{index}_{i}.jpg"
                print(f"Downloaded image {img_name}")

    except Exception as e:
        print(f"Error processing image {index}: {e}")
        continue

driver.quit()
