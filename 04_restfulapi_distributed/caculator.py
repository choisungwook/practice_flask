from flask_restful import Resource
from flask import jsonify

class Add(Resource):
  def get(self):
    print("a")
    return jsonify({'msg': 'hello'})


class Sub(Resource):
  def get(self):
    print("a")
    return jsonify({'msg': 'hello'})