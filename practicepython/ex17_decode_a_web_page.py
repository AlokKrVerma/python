import bs4
import requests

#print all titles
for link in bs4.BeautifulSoup(requests.get("https://www.nytimes.com").text, 'html.parser').find_all("h2", "story-heading"):
    print(link.get_text().replace("\n", " ").strip())

#print all links
# for link in bs4.BeautifulSoup(requests.get("https://www.nytimes.com").text, 'html.parser').find_all("a"):
#     print(link.get("href"))


