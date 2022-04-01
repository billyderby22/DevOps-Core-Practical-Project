from application import db

class Results(db.Model):
    pk = db.Column(db.Integer, primary_key = True)
    player = db.Column(db.String(100))
    team = db.Column(db.String(100))
    def __str__(self):
        return f"{self.player} plasy for {self.team}"