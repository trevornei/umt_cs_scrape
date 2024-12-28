import bs4
import requests
import json

url = "https://catalog.umt.edu/colleges-schools-programs/humanities-sciences/computer-science/bs-computer-science-software-engineering/" 


response = requests.get(url)

soup = bs4.BeautifulSoup(response.content, "html.parser")

table = soup.find('table', class_='sc_courselist')
# print(table.prettify())

# Iterates through each core_header/sub_table title.
for core_header in table.find_all('tr', class_='areaheader'):
    print(core_header.prettify())
# Create a class for sub_table.
class sub_table:
    
    def __init__(self, core_header, rows, school, course, credit_hour):
        self.core_header = core_header
        self.rows = []
        self.school = school
        self.course = course
        self.credit_hour = credit_hour
        # Create a nested class for each row.
        class row:
            def __init__(self, school, course, credit_hour):
                self.school = school
                self.course = course
                self.credit_hour = credit_hour

sub_tables = []


