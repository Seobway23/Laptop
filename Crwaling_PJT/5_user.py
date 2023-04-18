import requests
url = "https://google.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
requests = requests.get(url, headers=headers)
requests.raise_for_status()
with open("google.html", "w", encoding="utf8") as f:
    f.write(requests.text)


