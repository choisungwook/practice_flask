from flask import Flask
from flask_restful import Resource, Api
from caculator import Add, Sub

app = Flask(__name__)
api = Api(app)

api.add_resource(Add, '/add/')
api.add_resource(Sub, '/sub/')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8787, debug=True)