import json
from urllib.request import urlopen

with urlopen('http://localhost:5000/get_current_user') as response:
    # data = response.read()
    # data = data.decode('utf-8')
    # user = json.loads(data)
    user = json.load(response, encoding='utf-8')
    print(user)
