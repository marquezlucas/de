
import requests
import pandas as pd
import json

url = "https://cat-fact.herokuapp.com/facts"
headers = {"Accept-Encoding": "gzip, deflate"}

response = requests.get(url, headers=headers)
data = json.loads(response.text)
data
df = pd.DataFrame(data)
df.head()
