import os
from bs4 import BeautifulSoup

def merge_folder(feed_folder):
    feed_folder_name = feed_folder['name']

    posts = []

    for file in feed_folder['files'][1:]:
        file_path = f'feeds/{feed_folder_name}/{file}'

        with open(file_path,'rb') as feed_file:
            file_xml = feed_file.read()

        file_bs = BeautifulSoup(file_xml,'xml')

        posts+=file_bs.find_all('item')

    with open(f'feeds/{feed_folder_name}/merged.xml','wb') as merged:
        file = feed_folder['files'][0]
        file_path = f'feeds/{feed_folder_name}/{file}'

        with open(file_path,'rb') as feed_file:
            file_xml = feed_file.read()

        merged.write(file_xml)

        bs = BeautifulSoup(file_xml,'xml')

        items = bs.find('rss').find('channel')

        for post in posts:
            items.append(post)

        merged.write(bs.prettify().encode('utf-8'))

feed_folders = None
feed_folder_index = -1

for root, dirs, files in os.walk('feeds'):
    if not feed_folders:
        feed_folders = [{'name':dir,'files':[]} for dir in dirs]
    elif len(files) > 0 and 'temp' not in files:
        feed_folders[feed_folder_index]['files'] = files

    feed_folder_index+=1

index = 1

for feed_folder in feed_folders:
    feed_folder_name = feed_folder['name']
    print(f'{index}: {feed_folder_name}')
    index+=1

indices = [int(index)-1 for index in input('\nEnter the numbers for each feed you would like to merge (separate by comma if there is more than one feed number)\n>> ').replace(' ','').split(',')]

for index in indices:
    feed_folder = feed_folders[index]

    merge_folder(feed_folder)
