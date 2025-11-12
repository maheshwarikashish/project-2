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
        print("Scraping successful. Here is the extracted text:")
        # Extract and print the first 2000 characters of the text
        text = soup.get_text()
        print(text[:2000])