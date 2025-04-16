# coding=utf-8
import json
import pandas as pd
import requests

url = "http://113.24.212.22:8080/community/app"
data = {"process": "INFO", "id": 1}
res = requests.post(url, headers=headers, json=data,stream= False,timeout= 10)
