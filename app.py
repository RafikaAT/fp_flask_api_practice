from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers import movies
# from werkzeug import exceptions

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({'message': 'Hello from Flask!'}), 200

@app.route('/api/movies', methods=['GET', 'POST'])
def movies_handler():
    fns = {
        'GET': movies.index,
        'POST': movies.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code

@app.route('/api/movies/<int:cat_id>', methods=['GET', 'PATCH', 'PUT', 'DELETE'])
def movie_handler(cat_id):
    fns = {
        'GET': movies.show,
        'PATCH': movies.update,
        'PUT': movies.update,
        'DELETE': movies.destroy
    }
    resp, code = fns[request.method](request, cat_id)
    return jsonify(resp), code

# @app.errorhandler(exceptions.NotFound)
# def handle_404(err):
#     return {'message': f'Oops! {err}'}, 404

# @app.errorhandler(exceptions.BadRequest)
# def handle_400(err):
#     return {'message': f'Oops! {err}'}, 400

# @app.errorhandler(exceptions.InternalServerError)
# def handle_500(err):
#     return {'message': f"It's not you, it's us"}, 500

if __name__ == "__main__":
    app.run(debug=True)