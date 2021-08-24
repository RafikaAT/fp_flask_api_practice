from werkzeug.exceptions import BadRequest

movies = [
    {'id': 1, 'name': 'Harry Potter and The Prisoner of Azkaban', 'release_year': 2004},
    {'id': 2, 'name': 'The Hunger Games', 'release_year': 2012},
    {'id': 3, 'name': 'Divergent', 'release_year': 2014}
]

def index(req):
    return [c for c in movies], 200

def show(req, name):
    return find_by_name(name), 200

def create(req):
    new_movie = req.get_json()
    new_movie['id'] = sorted([c['id'] for c in movies])[-1] + 1
    movies.append(new_movie)
    return new_movie, 201

def destroy(req, name):
    movie = find_by_name(name)
    movies.remove(movie)
    return movie, 204

def find_by_name(name):
    try:
        return next(movie for movie in movies if movie['name'] == name)
    except:
        raise BadRequest(f"We don't have that movie with name {name}!")