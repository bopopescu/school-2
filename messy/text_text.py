import requests


header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'
    }
res = requests.get('http://127.0.0.1:8000/v1.0/forum/post/1/', headers=header)

print(res.text)