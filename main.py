#!/usr/bin/python
# coding=utf-8

import json
import requests

for line in open("mail.txt"): # Read mail list from file
    url = 'https://mail.example.com/api/v1/send/message' # API URL
    s = json.dumps(
        {
            'to': [line],
            'from': 'example@example.com',
            'sender': 'Example',
            'subject': 'Example Message',
            'plain_body': 'Hello World!'
        }
    )
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "X-Server-API-Key": "" # Your Server API KEY
        }
    r = requests.post(url, data=s, headers=headers)
    print r.text