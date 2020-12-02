import requests


r = requests.get("https://learneo.co")
print(r.status_code)
