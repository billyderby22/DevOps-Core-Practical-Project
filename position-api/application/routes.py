from flask import Flask, Response, request, jsonify
from application import app

@app.route('/position', methods=["POST"])
def position():
    team=request.get_json()['team']
    player=request.get_json()['player']

    if team == "West Ham":
        if player == 'Noble':
            position = 'Midfielder'
        elif player =='Antonio':
            position = 'Forward'
        elif player == 'Zouma':
            position = 'Defender'
        else: 
            position='invalid'
    elif team == "Arsenal":
        if player == 'White':
            position = 'Defender'
        elif player == 'Pepe':
            position = 'Forward'
        elif player == 'Xhaka':
            position = 'Midfielder'
        else: 
            position='invalid'
    elif team == "Man U":
        if player == 'Rashford':
            position = 'Forward'
        elif player == 'Maguire':
            position = 'Defender'
        elif player == 'Pogba':
            position = 'Midfielder'
        else: 
            position='invalid'
    elif team == "Liverpool":
        if player == 'Mane':
            position = 'Forward'
        elif player == 'Gomez':
            position = 'Defender'
        elif player == 'Thiago':
            position = 'Midfielder'
        else: 
            position='invalid'
    elif team == "Chelsea":
        if player == 'Chillwell':
            position = 'Defender'
        elif player == 'Kante':
            position = 'Midfielder'
        elif player == 'Werner':
            position = 'Forward'
        else: 
            position='invalid'

    return jsonify(position=position)
        