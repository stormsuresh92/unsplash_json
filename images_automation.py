import requests

def all_pages(pages):
    r = requests.get(f'https://unsplash.com/napi/search/photos?query=dog&per_page=20&page={x}&xp=')
    json_data = r.json()
    for data in json_data['results']:
        image_id = data['id']
        link = data['urls']['regular']
        with open(image_id + '.jpg', 'wb') as file:
            url_data = requests.get(link)
            file.write(url_data.content)
            
for x in range(0, 2):
    all_pages(x)