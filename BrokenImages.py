import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def find_broken_images(url):
    # Send a GET request to the URL
    response = requests.get(url)
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all the image tags on the page
    img_tags = soup.find_all('img')
    # Loop through all the image tags and check if the image URL is valid
    broken_image_urls = []

    for img in img_tags:
        img_url = img.get('src')
        if img_url:
            full_url = urljoin(url, img_url)
            response = requests.head(full_url)
            if response.status_code != 200 or 'image' not in response.headers['content-type']:
                broken_image_urls.append(full_url)

    if len(broken_image_urls) == 0:
        print(200)
    else:
        return broken_image_urls


url = input("Enter URL: ")
print(find_broken_images(url))