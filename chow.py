import requests
import json
from urllib import parse
import time
import random
from dotenv import load_dotenv
import os

load_dotenv()

chow_url = os.environ["CHOW_URL"]


num = random.random()

if  num > 0.95:
        
    url = "http://api.giphy.com/v1/gifs/random"

    params = parse.urlencode({
    "tag": "job application",
    "api_key": os.environ['KEY']
    })

    response = requests.get("".join((url, "?", params)))

    try:
        gif = response.json()['data']['images']['downsized_large']['url']

        chowmsg = {
            "content" : f"<@{os.environ['CHOW_ID']}>",
            "embeds":[{"image":{"url":f"{gif}"}}]
        }

        result = requests.post(chow_url, json = chowmsg)
    except:
        print(response)








    

