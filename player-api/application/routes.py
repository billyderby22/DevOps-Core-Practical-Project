from application import app
from flask import jsonify
from random import choice

players = ['Noble', 'Antonio', 'Zouma', 'Pepe', 'Xhaka', 'White', 'Rashford', 'Maguire', 'Pogba', 'Mane', 'Gomez', 'Thiago', 'Chillwell', 'Kante', 'Werner']

@app.route('/get-player', methods=['GET'])
def get_player():
    player = choice(players)
    return jsonify(player=player)