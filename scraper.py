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
    target_url = "http://quotes.toscrape.com/"
    
    print(f"Scraping {target_url}...")
    soup = scrape_website(target_url)
    
    if soup:
        # Extract the text
        text = soup.get_text()
        print(f"Length of scraped text: {len(text)}")

        # Save the scraped text to a file
        with open("scraped_data.txt", "w", encoding="utf-8") as f:
            f.write(text)
            
        print("Scraping successful. Data saved to scraped_data.txt")
    else:
        print("Scraping failed, soup object is None.")