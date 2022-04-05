from application import app
from flask_testing import TestCase
from flask import url_for

class TestBase(TestCase):
    def create_app(self):
        return app

class TestView(TestBase):
    def test_get_position_Noble(self):
        response = self.client.post(url_for('position'), json={"player":"Noble","team":"West Ham"})
        self.assert200(response)
        self.assertIn(b'Midfielder', response.data)