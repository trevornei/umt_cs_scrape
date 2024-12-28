import bs4
import requests
import random

url = "https://catalog.umt.edu/colleges-schools-programs/humanities-sciences/computer-science/bs-computer-science-software-engineering/" 

response = requests.get(url)

soup = bs4.BeautifulSoup(response.text, "html.parser")