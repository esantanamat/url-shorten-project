from flask import Blueprint, redirect, request, jsonify
from db import db
from functions import fetch_url, generate_short_url
from models import URL
routes = Blueprint("routes", __name__)

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
    shorten = fetch_url(shorten_name)
    if not shorten:
        return jsonify({'message': 'the shorten url does not exist'}), 400
    if request.method == 'GET':
        shorten.access_count +=1
        db.session.commit()
        return jsonify({
            'id': shorten.id,
            'original_url': shorten.original_url,
            'created_at': shorten.created_at,
            'updated_at': shorten.updated_at,
            'access_count': shorten.access_count
        }), 200
    if request.method == 'PUT':
        data = request.get_json()
        new_url = data.get('new_url')
        if not new_url:
            return jsonify({'error': 'New url is required'}), 400
        shorten.original_url = new_url
        db.session.commit()
        return jsonify({
            'message': f'the url has been updated to {new_url}'
        })
    if request.method == 'DELETE':
        db.session.delete(shorten)
        db.session.commit()
        return jsonify({'message': 'The URL has been deleted'
        }), 200

@routes.route('/shorten/<shorten_name>/stats', methods=['GET'])
def get_stats(shorten_name):
    shorten = fetch_url(shorten_name)
    if not shorten:
        return jsonify({'message': 'the shorten url does not exist'}), 400
    return jsonify({
        'access_count': shorten.access_count
    }), 200

@routes.route('/shorten/<shorten_name>/go', methods = ['GET'])
def re_route(shorten_name):
    shorten = fetch_url(shorten_name)
    if not shorten:
        return jsonify({'message': 'the shorten url does not exist'}), 400
    if shorten:
        return redirect(shorten.original_url)
    else:
        return jsonify({'message': 'mssing shorten name' }), 404