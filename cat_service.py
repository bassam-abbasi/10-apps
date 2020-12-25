import requests
import os
import shutil

def save_image(folder, cat_name, data):
    cat_full_name = os.path.abspath(os.path.join(folder,cat_name+'.jpg'))
    with open(cat_full_name,'wb') as fout:
        shutil.copyfileobj(data,fout)

def get_cats(folder,cat_name):
    url = 'http://consuming-python-services-api.azurewebsites.net/cats/random'
    response = requests.get(url, stream=True)
    data = response.raw
    save_image(folder, cat_name, data)