from application import app
from flask import request, jsonify

teams = dict(Noble='West Ham', White='Arsenal', Rashford='Man U', Mane='Liverpool', Chillwell='Chelsea')

@app.route('/team', methods=['POST'])
def noise():
    player_json = request.get_json()
    player = player_json["player"]
    return jsonify(team=teams[player])