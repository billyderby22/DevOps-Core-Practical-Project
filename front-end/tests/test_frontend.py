from application import app, db
from application.models import Results
from flask import url_for
import requests_mock
from flask_testing import TestCase

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db',
            DEBUG = True
        )
        return app
    
    def setUp(self):
        sample_result = Results(player='Noble', team='West Ham', position='Midfielder')
        db.create_all()
        db.session.add(sample_result)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestView(TestBase):
    def test_get_frontend(self):
        with requests_mock.Mocker() as m:
            m.get('http://player-api:5000/get-player', json={"player":"Mane"})
            m.get('http://team-api:5000/team', json={"team":"Liverpool"})
            m.post('http://position-api:5000/position', json={"position":"Forward"})
            response = self.client.get(url_for('index'))
            self.assert200(response)
            self.assertIn(b'Noble plays for West Ham and is a Midfielder', response.data)
            self.assertIn(b'Mane plays for Liverpool and is a Forward', response.data)