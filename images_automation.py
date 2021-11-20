import requests
import os
from alive_progress import alive_bar
from time import sleep

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'Connection':'keep-alive'
}

def all_pages(x):
    cur_dir = os.getcwd()
    images = cur_dir + '/' + f'{query}'
    if not os.path.exists(images):
        os.mkdir(images)
        
    url = f'https://unsplash.com/napi/search/photos?query={query}&per_page=20&page={x}&xp='
    r = requests.get(url, headers=headers)
    json_data = r.json()
    with alive_bar(20, title=f'Getting page {x}', bar='classic2', spinner='classic') as bar:
        for data in json_data['results']:
            image_id = data['id']
            link = data['urls']['regular']
            with open(images + '/' + image_id + '.jpg', 'wb') as file:
                url_data = requests.get(link)
                file.write(url_data.content)
            sleep(0.1)
            bar()

query = input('Enter keyword here:')
endpage = int(input('Enter end page:'))           
for x in range(1, endpage):
    all_pages(x)
    
print('\n')
print('Download finished')
input()
