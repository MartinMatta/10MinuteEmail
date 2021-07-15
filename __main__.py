import requests
from bs4 import BeautifulSoup


url = 'https://10minutemail.net/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


table = soup.find('mailbox-table')

table_row = table.find_all('tr')

print(table_row)

print(soup.find(id='fe_text').get("value"))
