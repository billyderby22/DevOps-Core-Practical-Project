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

    def test_get_position_Antonio(self):
        response = self.client.post(url_for('position'), json={"player":"Antonio","team":"West Ham"})
        self.assert200(response)
        self.assertIn(b'Forward', response.data)

    def test_get_position_Zouma(self):
        response = self.client.post(url_for('position'), json={"player":"Zouma","team":"West Ham"})
        self.assert200(response)
        self.assertIn(b'Defender', response.data)

    def test_get_position_Mane(self):
        response = self.client.post(url_for('position'), json={"player":"Mane","team":"Liverpool"})
        self.assert200(response)
        self.assertIn(b'Forward', response.data)

    def test_get_position_Gomez(self):
        response = self.client.post(url_for('position'), json={"player":"Gomez","team":"Liverpool"})
        self.assert200(response)
        self.assertIn(b'Defender', response.data)

    def test_get_position_Thiago(self):
        response = self.client.post(url_for('position'), json={"player":"Thiago","team":"Liverpool"})
        self.assert200(response)
        self.assertIn(b'Midfielder', response.data)

    def test_get_position_Chillwell(self):
        response = self.client.post(url_for('position'), json={"player":"Chillwell","team":"Chelsea"})
        self.assert200(response)
        self.assertIn(b'Defender', response.data)

    def test_get_position_Kante(self):
        response = self.client.post(url_for('position'), json={"player":"Kante","team":"Chelsea"})
        self.assert200(response)
        self.assertIn(b'Midfielder', response.data)

    def test_get_position_Werner(self):
        response = self.client.post(url_for('position'), json={"player":"Werner","team":"Chelsea"})
        self.assert200(response)
        self.assertIn(b'Forward', response.data)
   
    def test_get_position_Rashford(self):
        response = self.client.post(url_for('position'), json={"player":"Rashford","team":"Man U"})
        self.assert200(response)
        self.assertIn(b'Forward', response.data)

    def test_get_position_Pogba(self):
        response = self.client.post(url_for('position'), json={"player":"Pogba","team":"Man U"})
        self.assert200(response)
        self.assertIn(b'Midfielder', response.data)

    def test_get_position_Maguire(self):
        response = self.client.post(url_for('position'), json={"player":"Maguire","team":"Man U"})
        self.assert200(response)
        self.assertIn(b'Defender', response.data)

    def test_get_position_Pepe(self):
        response = self.client.post(url_for('position'), json={"player":"Pepe","team":"Arsenal"})
        self.assert200(response)
        self.assertIn(b'Forward', response.data)

    def test_get_position_Xhaka(self):
        response = self.client.post(url_for('position'), json={"player":"Xhaka","team":"Arsenal"})
        self.assert200(response)
        self.assertIn(b'Midfielder', response.data)

    def test_get_position_White(self):
        response = self.client.post(url_for('position'), json={"player":"White","team":"Arsenal"})
        self.assert200(response)
        self.assertIn(b'Defender', response.data)

   