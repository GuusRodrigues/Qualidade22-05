import json
from app import app

def test_get_usuarios():
    response = app.test_client().get('/usuarios')
    assert response.status_code == 200
    assert type(response.json) == list

def test_post_usuario_sucesso():
    novo_usuario = {"nome": "Gustavo", "email": "gustavo@gmail.com"}
    response = app.test_client().post('/usuarios', json=novo_usuario)
    assert response.status_code == 201
    assert response.json["nome"] == "Gustavo"

def test_post_usuario_erro():
    usuario_invalido = {"nome": "Gustavo"}
    response = app.test_client().post('/usuarios', json=usuario_invalido)
    assert response.status_code == 400
