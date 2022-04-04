from application import app
from flask import render_template
import requests 

@app.route('/')
def index():
    player = requests.get('http://player-api:5000/get-player')
    team = requests.post('http://team-api:5000/team', json=player.json())
    return f'{player.json()["player"]} plays for {team.json()["team"]}'
    return render_template('index.html', results = results)