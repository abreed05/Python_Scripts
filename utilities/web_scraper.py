# import required libraries
from bs4 import BeautifulSoup
import requests
import lxml
import time
import xlwt
import xlsxwriter

# Set various varibles including workbook variables 

n = int(input("Enter number of pages to iterate over "))
wb_name = input("Enter name of workbook ")
workbook = xlsxwriter.Workbook(wb_name + '.xlsx')
worksheet = workbook.add_worksheet()
row = 0
column = 0
# get web page 

base_link = input("Enter url minus page number for topic you want to scrape ")

for i in range (1, n+1):
    url = base_link+str(i)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")


# Find links, iterate over links and place them in the posts list 

    posts = []
    for link in soup.find_all('a', class_='PreviewTooltip'):
        posts.append(link.text)
        #time.sleep(1)
# export items in post list to excel workbook    

    for item in posts:
        worksheet.write(row, column, item)
        row += 1
workbook.close()
