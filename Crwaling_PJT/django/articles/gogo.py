import requests
from pprint import pprint

response = requests.get("http://127.0.0.1:8000/articles/json_3/")
result = response.json()


pprint(result)

# cd .. 상위 폴더 이동