from crypt import methods
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

items = []

@app.route('/items')
def get_items():
    return jsonify(items)

@app.route('/items/<id>', methods=['POST'])
def add_item(id):
    items.append(request.get_json())
    return '', 204

@app.route('/items/<id>', methods=['PUT'])
def edit_item(id):
    item = request.get_json()
    for i in range(len(items)):
        if items[i]['name'] == item['name']:
            items[i] = item
    return '', 204

@app.route('/items/<id>', methods=['DELETE'])
def delete_item(id):
    temp = []
    global items
    for i in items:
        if i['id'] != int(id):
            temp.append(i)
    items = temp
    return '', 204