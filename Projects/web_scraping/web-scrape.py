from bs4 import BeautifulSoup
import lxml
import requests

##############
# from file
##############

with open("./Projects/webscraping/website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "lxml")

first_heading = soup.find(name="h1")
specific_heading_class = soup.find(name="h1", class_="special")
specific_heading_id = soup.find(name="h1", id="yee")
all_headings = soup.find_all(name="h1")

print(first_heading)
print(specific_heading_class)
print(specific_heading_id)
print(all_headings)



##############
# from website
##############
response = requests.get("https://news.ycombinator.com/")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
print(soup.title)
