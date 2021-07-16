import requests
from bs4 import BeautifulSoup


url = 'https://10minutemail.net/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


table = soup.find('table')

table_rows = table.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row)


print(soup.find(id='fe_text').get("value"))
