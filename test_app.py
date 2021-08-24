import json

class TestAPICase():
    def test_welcome(self, api):
        res = api.get('/')
        assert res.status == '200 OK'
        assert res.json['message'] == 'Avada Kedavra!'

    def test_get_movies(self, api):
        res = api.get('/movies')
        assert res.status == '200 OK'
        assert res.json[0]['name'] == 'Harry Potter and The Prisoner of Azkaban'

    # def test_get_cat(self, api):
    #     res = api.get('/api/cats/2')
    #     assert res.status == '200 OK'
    #     assert res.json['name'] == 'Test Cat 2'

    def test_get_movies_error(self, api):
        res = api.get('/dogs')
        print(res.json)
        assert res.status == '400 BAD REQUEST'
        # assert "cat with id 4" in res.json['message']