import json
import os
import requests

with open('config.json') as config_file:
    config = json.load(config_file)

iteration = config['iteration']

print(f'Feed Download Iteration {iteration}')

os.mkdir(f'feeds/feed{iteration}')

feed_number = 1
max_results = config['max_results']
start_index = 0

while True:
    response = requests.get(config['blogger_url']+config['feed_url']+f'&max-results={max_results}'+(f'&start-index={start_index}' if start_index > 0 else ''))

    response_encoding = json.detect_encoding(response.content)
    response_decoded = response.content.decode(response_encoding)
    file_size = response.headers['Content-length']

    if response_decoded.count('<title') == 1:
        print("No additional post titles found. Terminating script")
        break

    print(f'Downloading {file_size} bytes (path="feed{iteration}/{start_index}-{max_results}.xml")')

    with open(f'feeds/feed{iteration}/{start_index}-{max_results}.xml','wb') as feed_file:
        feed_file.write(response.content)

    feed_number+=1
    start_index+=max_results

config['iteration']+=1

with open('config.json','w') as config_file:
    json.dump(config,config_file,indent='\t')
