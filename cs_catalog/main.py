import bs4
import requests
import json

url = "https://catalog.umt.edu/colleges-schools-programs/humanities-sciences/computer-science/bs-computer-science-software-engineering/" 


response = requests.get(url)

soup = bs4.BeautifulSoup(response.content, "html.parser")

# Snag the table
table = soup.find('table', class_='sc_courselist')

# Create bucket for sub_table class instances.
table_bucket = {}

current_header = None

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

for row in table.find_all('tr'):
    # Check for a header
    header = row.find('span', class_='courselistcomment')
    if header:
        current_header = header.text.strip()
        if current_header not in table_bucket:
            table_bucket[current_header] = sub_table(core_header=current_header)
        else:
            # Check if the row contains course details
            course_code_td = row.find('td', class_='codecol')
            course_name_td = row.find_all('td')[1] if len(row.find_all('td')) > 1 else None
            credit_hour_td = row.find('td', class_='hourscol')

            # If there is a course code and a name then snag the text for all three td's.
            if course_code_td and course_name_td:
                course_code = course_code_td.text.strip()
                course_name = course_name_td.text.strip()
                credit_hour = credit_hour_td.text.strip() if credit_hour_td else ""

                # Add the row to the current header...
                if current_header in table_bucket:
                    table_bucket[current_header].rows.append(
                        sub_table.row(course_code, course_name, credit_hour)
                    )
                

        
