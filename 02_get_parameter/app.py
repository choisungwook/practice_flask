from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def test():
    message = request.args.get('msg')
    return_data = {}

    if message is None:
      return_data = {'msg': 'empty'}
    else:
      return_data = {'msg': message}

    return jsonify(return_data)

if __name__=="__main__":
  app.run(host="127.0.0.1", port=8989, debug=True)