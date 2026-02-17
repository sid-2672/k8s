from flask import Flask, render_template,jsonify
from connections import collection
import os 

app = Flask(__name__)

PORT = os.environ.get('PORT', 8000)
@app.route('/')
def index():

    return jsonify({'message' : 'hello from backend'})

@app.route('/api/get')
def api():
    names = list(collection.find())
    result = []
    for name in names:
        result.append(name['value'])
    result = {
        'data' : result
    }
    return jsonify(result)

@app.route('/api/add/<name>')
def add_name(name):
    collection.insert_one({'value': name})
    return jsonify({'message': f'Name {name} added successfully'})

if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0') 