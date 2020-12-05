from flask_restful import Resource, reqparse
from flask import jsonify

class Add(Resource):
  def get(self):
    parser = reqparse.RequestParser(bundle_errors=True)
    parser.add_argument('operand1', type=int, required=True, help='operand1 is required The detail error is{error_msg}')
    parser.add_argument('operand2', type=int, required=True, help='operand2 is required. The detail error is {error_msg}')
    args = parser.parse_args()

    operand1 = args['operand1']
    operand2 = args['operand2']

    return jsonify({'result': operand1+operand2})


class Sub(Resource):
  def get(self):
    parser = reqparse.RequestParser(bundle_errors=True)
    parser.add_argument('operand1', type=int, required=True, help='operand1 is required The detail error is{error_msg}')
    parser.add_argument('operand2', type=int, required=True, help='operand2 is required. The detail error is {error_msg}')
    args = parser.parse_args()

    operand1 = args['operand1']
    operand2 = args['operand2']
    return jsonify({'result': operand1 - operand2})