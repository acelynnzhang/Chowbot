import requests
import json
from urllib import parse
import time
import random
from dotenv import load_dotenv
import os

load_dotenv()

chow_url = os.getenv('CHOW_URL')

hours = 0
goal = 0

while True:
    if hours == goal:
            
        url = "http://api.giphy.com/v1/gifs/random"

        params = parse.urlencode({
        "tag": "job application",
        "api_key": os.getenv('KEY')
        })

        response = requests.get("".join((url, "?", params)))

        gif = response.json()['data']['images']['downsized_large']['url']

        chowmsg = {
                    "content" : f"<@{os.getenv('CHOW_ID')}>",
                    "embeds":[{"image":{"url":f"{gif}"}}]
                }

        result = requests.post(chow_url, json = chowmsg)

        goal = random.randint(1, 72)
        hours = 0

    time.sleep(3600)
    hours += 1


        

