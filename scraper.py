import requests
from bs4 import BeautifulSoup
import time
import random

def search_google(dork, max_results=10):
    """
    Performs a Google search for a given dork and returns a list of result URLs.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; Webscrapper-Dorker/1.0; +https://github.com/yourusername/webscrapper-dorker)"
    }
    # Use Google search URL
    url = "https://www.google.com/search"
    params = {"q": dork, "num": max_results}
    try:
        # Sleep randomly to avoid quick repeat hits
        time.sleep(random.uniform(1, 3))
        resp = requests.get(url, headers=headers, params=params, timeout=10)
        if "unusual traffic" in resp.text.lower():
            print("  [!] Blocked by Google (unusual traffic detected). Try again later.")
            return []
        soup = BeautifulSoup(resp.text, "html.parser")
        links = []
        for g in soup.find_all('a'):
            href = g.get('href')
            if href and href.startswith("/url?q="):
                real_url = href.split("/url?q=")[1].split("&")[0]
                if not real_url.startswith("https://webcache.googleusercontent.com"):
                    links.append(real_url)
        return links
    except Exception as e:
        print(f"  [!] Error: {e}")
        return []
