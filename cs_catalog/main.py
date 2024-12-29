import bs4
import requests
import json

url = "https://catalog.umt.edu/colleges-schools-programs/humanities-sciences/computer-science/bs-computer-science-software-engineering/" 


response = requests.get(url)

soup = bs4.BeautifulSoup(response.content, "html.parser")

table = soup.find('table', class_='sc_courselist')
# print(table.prettify())

# Create a list to store sub_tables.
sub_tables_list = ['Core Courses', 'Science Core', 'Science Electives', 'Communications Requirement', 'Software Engineering Core', 'Advanced Software Electives', 'Upper Division CS Electives']

# Define the class before using it
class sub_table:
    def __init__(self, core_header, school, course, credit_hour):
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
    'core_courses': sub_table(None, None, None, None),
    'science_core': sub_table(None, None, None, None),
    'science_electives': sub_table(None, None, None, None),
    'communications_requirement': sub_table(None, None, None, None),
    'software_engineering_core': sub_table(None, None, None, None),
    'advanced_software_electives': sub_table(None, None, None, None),
    'upper_division_cs_electives': sub_table(None, None, None, None)
}

for header in table.find_all('tr', class_='areaheader'):
    core_header = header.text
    print(type(core_header)) 
    
    # Checks if core_header matches any of the indeces in the sub_tables_list.
    if core_header in sub_tables_list:
        print(f"core_header: {core_header}")


    '''
    
    for row in header.find_next('tbody').find_all('tr'):
        columns = row.find_all('td')
        if len(columns) == 3:
            school = columns[0].text.strip()
            course = columns[1].text.strip()
            credit_hour = columns[2].text.strip()
            sub_tables.append(sub_table(core_header, school, course, credit_hour))
   '''         