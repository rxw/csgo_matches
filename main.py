#!bin/python

import json
import requests

if __name__ == '__main__':
    with open('creds.json', 'r') as f:
        json_creds = f.read()
        creds = json.loads(json_creds)

    api_url = 'https://api.pandascore.co'
    stats_url = '/csgo/matches'
    r = requests.get(api_url + stats_url, params=creds)
    print(r.text)
