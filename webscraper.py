from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://thesiswhisperer.com').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('data.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['header', 'date', 'summary'])

for article in soup.find_all('article'):
    header = article.h1.a.text
    #print(header)
    date = article.find('div', class_='entry-meta').a.time.text
    #print(date)
    summary = article.find('div', class_='entry-summary').p.text
    #print(summary)
    #print('\n\n\n')
    csv_writer.writerow([header, date, summary])

csv_file.close()