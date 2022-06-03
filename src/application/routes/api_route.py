from flask import Blueprint, jsonify, request
from src.application.adapter.api_adapter import flask_adapter
from src.application.composer.add_restaurant_composite import add_restaurant_composer
from src.application.composer.get_restaurant_composite import get_restaurant_composer
from src.application.composer.delete_restaurant_composite import delete_restaurant_composer
from src.application.composer.update_restaurant_composite import update_restaurant_composer


routes_blue_print = Blueprint("api_routes", __name__)

@routes_blue_print.route("/api/restaurant/<int:id>", methods = ["GET"])
@routes_blue_print.route("/api/restaurant", methods = ["GET"])
def get_restaurant(id = None):

    if isinstance(id, int):
        request.args = {'id': id}
    response = flask_adapter(request = request, route = get_restaurant_composer())

    return jsonify({
        'data': response.body
    }), response.code

@routes_blue_print.route("/api/restaurant/<int:id>", methods = ["DELETE"])
def delete_restaurant(id):

    request.args = {'id': id}
    response = flask_adapter(request = request, route = delete_restaurant_composer())

    return jsonify({
        'data': response.body
    }), response.code

@routes_blue_print.route("/api/restaurant/<int:id>", methods = ["PUT"])
def update_restaurant(id):

    request.args = {'id': id}
    response = flask_adapter(request = request, route = update_restaurant_composer())

    return jsonify({
        'data': response.body
    }), response.code

@routes_blue_print.route("/api/restaurant", methods = ["POST"])
def add_restaurant():

    response = flask_adapter(request = request, route = add_restaurant_composer())

    return jsonify({
        'data': response.body
    }), response.code
