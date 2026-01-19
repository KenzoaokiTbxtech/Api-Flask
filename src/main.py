from flask import Flask, request
from db import db
from models import Animais


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///meudatabase.db"
db.init_app(app)

@app.route("/")
def index():
    return "API de Animais funcionando!"

@app.route("/animais", methods=["GET", "POST", "PUT", "DELETE"])
def animais():
    if request.method == "GET":
        animais = db.session.query(Animais).all()
        return {"animais": [repr(animal) for animal in animais]}, 200
        
    elif request.method == "POST":
        data = request.get_json()
        nome = data.get("nome")
        especie = data.get("especie")
        idade = data.get("idade")

        novo_animal = Animais(nome=nome, especie=especie, idade=idade)
        db.session.add(novo_animal)
        db.session.commit()
        return {"mensagem": "Animal adicionado com sucesso!"}, 201

    elif request.method == "PUT":

        data = request.get_json()
        animal_id = data.get("id")
        nome = data.get("nome")
        especie = data.get("especie")
        idade = data.get("idade")

        animal = db.session.get(Animais, animal_id)
        if animal:
            if nome:
                animal.nome = nome
            if especie:
                animal.especie = especie
            if idade:
                animal.idade = idade
            db.session.commit()
            return {"mensagem": "Animal atualizado com sucesso!"}, 200
        else:
            return {"mensagem": "Animal não encontrado."}, 404
    
    elif request.method == "DELETE":
        data = request.get_json()
        animal_id = data.get("id")
        animal = db.session.get(Animais, animal_id)
        if animal:
            db.session.delete(animal)
            db.session.commit()
            return {"mensagem": "Animal excluído com sucesso!"}, 200
        else:
            return {"mensagem": "Animal não encontrado."}, 404

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', debug=True)