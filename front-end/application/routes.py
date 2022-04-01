from application import app, db
from application.models import Results
from flask import render_template
import requests

@app.route('/')
def index():
    player = requests.get('http://player-api:5000/get-player')
    team = requests.post('http://team-api:5000/team', json=player.json())
    db.session.add(Results(player=player.json()["player"], team=team.json()["team"]))
    db.session.commit()
    results = Results.query.all()
    return render_template('index.html', results = results)