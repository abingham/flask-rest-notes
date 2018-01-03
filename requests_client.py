import requests


r = requests.get('http://localhost:5000/get_current_user')
print(r.json())
