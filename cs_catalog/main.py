import bs4
import requests
import json

url = "https://catalog.umt.edu/colleges-schools-programs/humanities-sciences/computer-science/bs-computer-science-software-engineering/" 


response = requests.get(url)

soup = bs4.BeautifulSoup(response.content, "html.parser")

table = soup.find('table', class_='sc_courselist')
print(table.prettify())

header = table.find_all('span', class_='courselistcomment areaheader')
print(f'Whoa, these are the headers: {header}')

row = header.find_next('tr')
for td in row:
    td.find_all('td')
    print(td)

# Create a list to store sub_tables.
# sub_tables_list = ['Core Courses', 'Science Core', 'Science Electives', 'Communications Requirement', 'Software Engineering Core', 'Advanced Software Electives', 'Upper Division CS Electives']

# Define the class before using it
class sub_table:
    def __init__(self, core_header=None):
        self.core_header = core_header
        self.rows = []
        # Create a nested class for each row.
        class row:
            def __init__(self, school, course, credit_hour):
                self.school = school
                self.course = course
                self.credit_hour = credit_hour

# Correct the dictionary definition and instantiation
table_bucket = {
    'core_courses': sub_table(None),
    'science_core': sub_table(None),
    'science_electives': sub_table(None),
    'communications_requirement': sub_table(None),
    'software_engineering_core': sub_table(None),
    'advanced_software_electives': sub_table(None),
    'upper_division_cs_electives': sub_table(None)
}

for header in table.find_all('tr', class_='courselistcomment areheader'):
    print(header.text.strip())  
    #     table_bucket['upper_division_cs_electives'].core_header = header.text

# print(table_bucket)