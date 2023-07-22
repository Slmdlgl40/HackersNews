import requests
from bs4 import BeautifulSoup

link = "https://news.ycombinator.com/"
response = requests.get(link)
link_filter = "http"

soup = BeautifulSoup(response.text, "html.parser")
for link in soup.find_all("a", rel="noreferrer"):
    found_link = link.get("href")
    if link_filter in found_link:
        print(found_link)