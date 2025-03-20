from flask import Blueprint, request, jsonify

routes = Blueprint("routes", __name__)

@routes.route('/')
def home():
    return "Hello from Home :D "

@routes.route('/hello/<name>')
def hello_name(name):
    return f'Hello {name}!'

@routes.route('/shorten', methods=['POST'])
def shorten(): 
    return 'test'

@routes.route('/shorten/<shorten_name>', methods=['PUT', 'GET', 'DELETE'])
def handle_shorten_by_id(shorten_name):
    if request.method == 'GET':
        return 'hi'

@routes.route('/shorten/<shorten_name>/<stats>', methods=['GET'])
def get_stats(shorten_name, stats):
    return shorten_name, stats
