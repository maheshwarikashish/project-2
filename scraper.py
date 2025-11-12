import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    """
    This function takes a URL as input, scrapes the website content,
    and returns a BeautifulSoup object.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    except requests.exceptions.RequestException as e:
        print(f"Error scraping {url}: {e}")
        return None

if __name__ == "__main__":
    target_url = "https://www.indiehackers.com/blog"
    
    print(f"Scraping {target_url}...")
    soup = scrape_website(target_url)
    
    if soup:
        print("Scraping successful. Here is the raw HTML:")
        # Print the first 3000 characters of the prettified HTML
        print(soup.prettify()[:3000])
