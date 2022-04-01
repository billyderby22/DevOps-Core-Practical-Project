from application import app
from flask import request, jsonify

teams = dict(Mark Noble='West Ham', Ben White='Arsenal', Marcus Rashford='Man U', Sadio Mane='Liverpool', Ben Chillwell='Chelsea')

@app.route('/team', methods=['POST'])
def noise():
    player_json = request.get_json()
    player = player_json["player"]
    return jsonify(team=teams[player])