from application import app
import requests

@app.route('/')
def index():  #home root
    name = requests.get('http://name-api:5000/get-name')
    stats = requests.post('http://stats-api:5000/stats', json=name.json())
    return f'{name.json()["name"]} goes {stats.json()["stats"]}'

