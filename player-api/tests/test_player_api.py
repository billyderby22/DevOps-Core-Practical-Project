from application import app
import application.routes
from flask_testing import TestCase
from unittest.mock import patch
from flask import url_for

class TestBase(TestCase):
    def create_app(self):
        return app

class TestView(TestBase):
  
    def test_get_player(self):
        with patch ('application.routes.choice') as r:
            r.return_value = 'Noble'
            response = self.client.get(url_for('get_player'))
            self.assert200(response)
            self.assertIn(b'Noble', response.data)
    
  