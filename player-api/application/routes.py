from application import app
from flask import jsonify
from random import choice

players = ['Noble', 'White', 'Rashford', 'Mane', 'Chillwell']

@app.route('/get-player', methods=['GET'])
def get_player():
    player = choice(players)
    return jsonify(player=player)