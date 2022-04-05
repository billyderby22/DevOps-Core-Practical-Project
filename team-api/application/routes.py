from application import app
from flask import request, jsonify
from random import choice

teams = ('West Ham', 'Arsenal', 'Man U', 'Liverpool', 'Chelsea')

@app.route('/team', methods=['GET'])
def noise():
    team=choice(teams)
    return jsonify(team=team)