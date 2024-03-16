import requests
from bs4 import BeautifulSoup

#URL = "https://www.nike.com/ca/size-fit/womens-leggings"

#print (page.text)

def get_tables(URL):
    agent = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    page = requests.get(URL, headers=agent)
    soup = BeautifulSoup(page.content, "html.parser")
    html_content = soup.find_all("table", class_="size-chart-table")

    #for result in results:
        #print(result,end="/n"*4)

    #id = "4420c434-4749-4fa6-aaa1-9041f02a56d6"

    formatted_data = []

    for table in soup.find_all('table', class_='size-chart-table'):
        table_data = []
        for row in table.find_all('tr'):
            row_data = [cell.get_text(strip=True) for cell in row.find_all(['th', 'td'])]
            table_data.append(row_data)
        formatted_data.append(table_data)
    print(formatted_data)
    finale = []
    for y in range(len(formatted_data[0][0])):
        finale1 = []
        for i in range(len(formatted_data[0])):
            finale1.append(formatted_data[0][i][y])
        finale.append(finale1)
        print(finale1)

    print(finale)

#URLS = ["https://www.nike.com/ca/size-fit/mens-footwear", ""]

URL = "https://www.nike.com/ca/size-fit/mens-footwear"
get_tables(URL)

