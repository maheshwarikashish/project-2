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
    # Example Usage:
    # We will need to find a good website to scrape for business problems.
    # For now, let's use a placeholder.
    target_url = "https://www.indiehackers.com" # Replaced placeholder with a real target URL
    
    print(f"Scraping {target_url}...")
    soup = scrape_website(target_url)
    
    if soup:
        # In the next step, we will add logic here to extract and process the text.
        print("Scraping successful. Next, we will process the text to find keywords.")
        # For now, let's just print the title
        print(f"Page Title: {soup.title.string}")