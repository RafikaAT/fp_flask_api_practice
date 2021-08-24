from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers import movies
from werkzeug import exceptions

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({'message': 'Avada Kedavra!'}), 200

@app.route('/movies', methods=['GET', 'POST'])
def movies_handler():
    fns = {
        'GET': movies.index,
        'POST': movies.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code

@app.route('/movies/<string:name>', methods=['GET', 'DELETE'])
def movie_handler(name):
    fns = {
        'GET': movies.show,
        'DELETE': movies.destroy
    }
    resp, code = fns[request.method](request, name)
    return jsonify(resp), code

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return '<h1 style="text-align:center">Error: this_page_does_not_exist</h1><img src="https://memegenerator.net/img/instances/82218331.jpg" style="display: block; margin: auto; padding-top: 10%"/>', 404

@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return '<h1 style="text-align:center">Error: this_movie_does_not_exist</h1><img src="https://memegenerator.net/img/instances/64370322.jpg" style="display: block; margin: auto; padding-top: 10%"/>', 400


if __name__ == "__main__":
    app.run(debug=True)