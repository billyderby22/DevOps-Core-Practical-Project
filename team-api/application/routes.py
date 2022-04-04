from application import app
from flask import request, jsonify

teams = dict(Noble='West Ham', Antonio='West Ham', Zouma='West Ham', Pepe='Arsenal', White='Arsenal', Xhaka='Arsenal', Rashford='Man U', Maguire='Man U', Pogba='Man U', Gomez='Liverpool', Thiago='Liverpool', Mane='Liverpool', Chillwell='Chelsea', Kante='Chelsea', Werner='Chelsea')

@app.route('/team', methods=['POST'])
def noise():
    player_json = request.get_json()
    player = player_json["player"]
    return jsonify(team=teams[player])