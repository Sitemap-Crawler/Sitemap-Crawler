import requests
from bs4 import BeautifulSoup

# Function to detect broken images
def detect_broken_images(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the request was unsuccessful

        soup = BeautifulSoup(response.content, 'html.parser')
        images = soup.find_all('img')
        for image in images:
            src = image.get('src')
            image_response = requests.get(src)
            if image_response.status_code != 200:
                print(f'Error: {image_response.status_code} - Broken image link: {src}')

    except Exception as e:
        print(f'Error: {e}')

# Define the base URL of the sitemap
sitemap_url = 'https://example.com/sitemap.xml'

try:
    # Send a GET request to the sitemap URL and parse the response
    response = requests.get(sitemap_url)
    response.raise_for_status()

    sitemap = BeautifulSoup(response.content, 'xml')

    # Extract the URLs from the sitemap
    urls = []
    for url in sitemap.find_all('url'):
        loc = url.find('loc').text
        urls.append(loc)

    # Crawl each URL in the sitemap
    for url in urls:
        # Send a GET request to the URL
        response = requests.get(url)
        if response.status_code == 200:
            # Parse the response
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract links from the page
            links = soup.find_all('a')

            # Process each link
            for link in links:
                href = link.get('href')
                # Do whatever you want with the extracted link, e.g. print it
                print(href)

            # Detect broken images in the page
            detect_broken_images(url)

        else:
            print(f'Error: {response.status_code} - Failed to crawl URL: {url}')

except Exception as e:
    print(f'Error: {e}')
