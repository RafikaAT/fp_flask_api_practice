import pytest
import app
from controllers import movies

@pytest.fixture
def api(monkeypatch):
    test_movies = [
    {'id': 1, 'name': 'Harry Potter and The Prisoner of Azkaban', 'release_year': 2004},
    {'id': 2, 'name': 'The Hunger Games', 'release_year': 2012},
    {'id': 3, 'name': 'Divergent', 'release_year': 2014}
]
    monkeypatch.setattr(movies, "movies", test_movies)
    api = app.app.test_client()
    return api