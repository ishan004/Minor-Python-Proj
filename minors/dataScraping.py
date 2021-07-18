import requests
from bs4 import BeautifulSoup

r = requests.get("https://english.onlinekhabar.com/")

soup = BeautifulSoup(r.content, 'html.parser')

sidebar = soup.find_all(class_="ok-news-post")

print(sidebar)