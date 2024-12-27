import bs4
import requests
import random

url = "https://catalog.umt.edu/colleges-schools-programs/humanities-sciences/computer-science/bs-computer-science-software-engineering/" 

response = requests.get(url)

soup = bs4.BeautifulSoup(response.text, "html.parser")

"""
Notes about the Table(s):
- There is technically only one table but there are many sub-tables.
- Each sub-table has a unique structure of 
    "<tr>
        <td>
            <span>

            </span>
        </td>
    </tr>"

    Each sub-table has class="even areheader"
    ---> We can isolate each sub-data type by selecting for the "areheader" class.

Create a variable for each table.

"""

