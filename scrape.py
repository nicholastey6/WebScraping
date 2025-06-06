import requests
from bs4 import BeautifulSoup

def fetch_titles(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch page: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    # Example: Fetch all h2 elements with class "post-title"
    titles = soup.find_all('h2', class_='post-title')
    return [title.get_text(strip=True) for title in titles]

if __name__ == "__main__":
    url = "https://example.com/blog"
    titles = fetch_titles(url)

    print("Blog Titles Found:")
    for i, title in enumerate(titles, 1):
        print(f"{i}. {title}")
