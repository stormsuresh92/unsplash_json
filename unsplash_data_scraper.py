import requests
import csv

datalist = []

def all_pages(pages):
    r = requests.get(f'https://unsplash.com/napi/search/photos?query=dog&per_page=20&page={x}&xp=')
    json_data = r.json()
    for data in json_data['results']:
        image_id = data['id']
        alt_description = data['alt_description']
        link = data['urls']['regular']
        datalist.append([image_id, alt_description, link])
        with open('output_data.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(datalist)
                
for x in range(0, 50):
    all_pages(x)