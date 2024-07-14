from behave import given, when, then
import requests

BASE_URL = 'http://localhost:8002'

@given('que eu tenho os detalhes do pedido')
def step_impl(context):
    context.pedido_data = {
        'valor': '7.50',
        'quantidade': '1',
        'produto_id': '1',
        'cliente_id': '1',
        'descricao': 'Acompanhamentos',
        'status': 'RECEBIDO'
    }

@given('que eu tenho os detalhes atualizados do pedido')
def step_impl(context):
    context.updated_pedido_data = {
        'valor': '7.50',
        'quantidade': '1',
        'produto_id': '1',
        'cliente_id': '1',
        'descricao': 'Acompanhamentos',
        'status': 'EM_PREPARACAO'
    }

@when('eu faço o cadastro de um pedido')
def step_impl(context):
    context.response = requests.post(f"{BASE_URL}/pedidos/create", json=context.pedido_data)

@when('eu faço uma atualização de um pedido')
def step_impl(context):
    context.response = requests.put(f"{BASE_URL}/pedidos/update/1", json=context.updated_pedido_data)

@when('eu faço a consulta dos pedidos cadastros')
def step_impl(context):
    context.response = requests.get(f"{BASE_URL}/pedidos")

@when('eu faço a exclusão de um pedido')
def step_impl(context):
    context.response = requests.delete(f"{BASE_URL}/pedidos/delete/1")

@then('eu devo receber uma resposta com o código de status 201')
def step_impl(context):
    assert context.response.status_code == 201

@then('eu devo receber uma resposta com o código de status 200')
def step_impl(context):
    assert context.response.status_code == 200
