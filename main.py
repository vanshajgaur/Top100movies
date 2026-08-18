from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(response.text, 'html.parser')

titles = []

title = soup.find_all("h3", class_="title")
for _ in title:
    titles.append(_.text)
new = list(reversed(titles))
print(new)





