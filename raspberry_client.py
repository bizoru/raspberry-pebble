import requests

base_url = "http://localhost:3412/status"
r = requests.get(base_url)

result = r.json()
print result['status']
