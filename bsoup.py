import requests
from bs4 import BeautifulSoup
import os

def fetch_image_urls(query, num_images=5):
    search_url = "https://www.google.com/search?hl=en&tbm=isch&q=" + query

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    }

    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    image_elements = soup.find_all('div', attrs={'data-attrid': 'images universal'})
    image_urls = []
    for image_element in image_elements[0]:
        anchor = image_element.find_all("a")
        print(anchor)

    return image_urls


if __name__ == "__main__":
    query = "sunset scenery"
    num_images = 5

    print(f"Fetching images for query: {query}")
    image_urls = fetch_image_urls(query, num_images)
