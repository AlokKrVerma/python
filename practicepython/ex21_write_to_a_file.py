import bs4
import requests

#store all titles in file
with open("Ex21_output.txt", 'w+') as file_open:
    for link in bs4.BeautifulSoup(requests.get("https://www.nytimes.com").text, 'html.parser').find_all("h2", "story-heading"):
        file_open.writelines(link.get_text().replace("\n", " ").strip() + "\n")