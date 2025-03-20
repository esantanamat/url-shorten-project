from flask import Blueprint, request, jsonify
from db import db
from functions import generate_short_url
from models import URL
routes = Blueprint("routes", __name__)

@routes.route('/')
def home():
    return "Hello from Home :D "

@routes.route('/hello/<name>')
def hello_name(name):
    return f'Hello {name}!'

@routes.route('/shorten', methods=['POST'])
def shorten(): 
    if request.method == 'POST':
        data = request.get_json()
        original_url = data.get('original_url')
        if not original_url:
            return jsonify({"error": "No url provided"}), 400
        short_url = generate_short_url()
        new_url = URL(original_url=original_url, short_url=short_url)
        db.session.add(new_url)
        db.session.commit()
    return jsonify({"short_url": short_url}), 201


@routes.route('/shorten/<shorten_name>', methods=['PUT', 'GET', 'DELETE'])
def handle_shorten_by_id(shorten_name):
    if request.method == 'GET':
        db.session.query(URL).filter_by(short_url=shorten_name).first()
        return jsonify({
            'id': shorten.id,
            'original_url': shorten.original_url,
            'created_at': shorten.created_at,
            'updated_at': shorten.updated_at,
            'access_count': shorten.access_count
        })

@routes.route('/shorten/<shorten_name>/<stats>', methods=['GET'])
def get_stats(shorten_name, stats):
    t = shorten_name
    s = stats
    return f"{t}, {s}"
