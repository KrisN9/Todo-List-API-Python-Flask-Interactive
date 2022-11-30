from flask import Flask
from flask import jsonify
from flask import request
import json
app = Flask(__name__)

todos = [
    {"label": "My first task", "done": False}
]

@app.route('/todos', methods=['GET'])
def get_todos():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    print("Incoming request with the following body", request_body)
    request.data = json.loads(todos)
    return jsonify(request.data)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)