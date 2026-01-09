from db import db

class Animais(db.Model):
    __tablename__ = 'animais'

    id = db.Column(db.INTEGER, primary_key = True)
    nome = db.Column(db.String(40), nullable = False)
    especie = db.Column(db.String(40), nullable = False)
    idade = db.Column(db.String(20), nullable = False)

    def __repr__(self):
        return f'Animal: {self.nome}, {self.especie}, {self.idade}'