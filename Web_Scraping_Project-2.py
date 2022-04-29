from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import requests
import pandas

url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page = requests.get(url)
soup = BeautifulSoup(page.text,'html.parser')
star_table = soup.find_all('table')
table_rows = star_table[7].find_all('tr')
whole_data = []

for tr in table_rows.find_all("tr"):
    td_tags = soup.find_all("td")
    whole_data.append(td_tags)

data_f = pandas.DataFrame(whole_data)
csv_file = data_f.to_csv("Scraper.csv")

with open("Scraper.csv",'w') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerows(csv_file)