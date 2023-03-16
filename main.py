import requests
from bs4 import BeautifulSoup

def crawl_sitemap():
    # Prompt user to input sitemap URL
    url = input("Enter sitemap URL: ")

    # Send a GET request to the sitemap URL
    response = requests.get(url)

    # Parse the sitemap XML using BeautifulSoup with lxml parser
    soup = BeautifulSoup(response.text, 'lxml')

    # Find all the URLs in the sitemap
    urls = [loc.text for loc in soup.find_all('loc')]

    # Crawl each URL and print the response status code
    for url in urls:
        response = requests.get(url)
        print(f'{url}: {response.status_code}')

# Example usage: call the function to prompt the user for the sitemap URL
crawl_sitemap()
