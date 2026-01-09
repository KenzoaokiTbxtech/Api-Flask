import pytest
from main import app, db


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client


def test_api_funcionando(client):
    response = client.get('/')
    assert response.status_code == 200


def test_criar_animal(client):
    response = client.post('/animais', json={"nome": "Rex", "especie": "Cachorro", "idade": "5"})
    assert response.status_code == 201


def test_listar_animais(client):
    response = client.get('/animais')
    assert response.status_code == 200


def test_atualizar_animal(client):
    client.post('/animais', json={"nome": "Mia", "especie": "Gato", "idade": "3"})
    response = client.put('/animais', json={"id": 1, "nome": "Mia Updated"})
    assert response.status_code == 200


def test_deletar_animal(client):
    client.post('/animais', json={"nome": "Bolt", "especie": "Coelho", "idade": "1"})
    response = client.delete('/animais', json={"id": 1})
    assert response.status_code == 200
