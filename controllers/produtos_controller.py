from flask import Blueprint, jsonify, request
from models.produtos import products
from config.jwt_config import token_required

produtos_bp = Blueprint('produtos', __name__)

@produtos_bp.route('/products')
@token_required
def listar_produtos():
    preco_asc = request.args.get('preco_asc')
    preco_desc = request.args.get('preco_desc')
    desc_part = request.args.get('description_part')

    lista = products.copy()

    if preco_asc:
        lista.sort(key=lambda x: x['product_price'])
    elif preco_desc:
        lista.sort(key=lambda x: x['product_price'], reverse=True)
    elif desc_part:
        lista = [p for p in lista if desc_part.lower() in p['product_description'].lower()]

    return jsonify(lista)

@produtos_bp.route('/products/<int:id>')
@token_required
def get_produto(id):
    for produto in products:
        if produto["id"] == id:
            return jsonify(produto)
    return jsonify({'message': 'produto nao encontrado'}), 404
