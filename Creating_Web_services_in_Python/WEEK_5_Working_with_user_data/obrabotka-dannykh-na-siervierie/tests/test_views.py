import json
from .factories import ItemFactory, ReviewFactory
from somemart.models import Item, Review


class TestViews(object):
    def test_post_item(self, client, db):
        """/api/v1/goods/ (POST) сохраняет товар в базе."""
        url = '/api/v1/goods/'
        #data = json.dumps({"title": "Gouda cheese", "description": "The number one cheese in the world", "price": 100})
        data = json.dumps({'title': 'Сыр "Российский"','description': 'Очень вкусный сыр, да еще и российский.','price': 100 })
        response = client.post(url, data = data, content_type='application/json')
        assert response.status_code == 201
        document = response.json()
        # Объект был сохранен в базу
        item = Item.objects.get(pk=document['id'])
        assert item.title == 'Сыр "Российский"'
        assert item.description == 'Очень вкусный сыр, да еще и российский.'
        assert item.price == 100

    def test_post_review(self, client, db):
        url = '/api/v1/goods/'
        item = ItemFactory()

        data = json.dumps({
            'text': 'Best. Cheese. Ever.',
            'grade': 9
        })
        response = client.post(url+f"{item.id}/reviews/", data=data, content_type='application/json')
        assert response.status_code == 201
        review_document = response.json()

        item_reviews = Item.objects.get(pk=item.id).review_set.all()
        review = [r for r in item_reviews if r.id == review_document['id']]

        assert len(review) == 1
        review = review[0]
        assert review.text == 'Best. Cheese. Ever.'
        assert review.grade == 9

        response = client.post(url+f"{1000}/reviews/", data=data, content_type='application/json')
        assert response.status_code == 404

        data = json.dumps({
            'text': 'Best. Cheese. Ever.',
            'grade': -3
        })
        response = client.post(url+f"{item.id}/reviews/", data=data, content_type='application/json')
        assert response.status_code == 400


    def test_get_item(self, client, db):
        url = '/api/v1/goods/'
        item = ItemFactory()
        reviews = []

        response = client.get(url + f"{item.id}/")
        assert response.status_code == 200
        response_document = response.json()
        assert len(response_document['reviews']) == 0

        reviews.extend(ReviewFactory.create_batch(size=3, item=item))

        response = client.get(url + f"{item.id}/")
        assert response.status_code == 200
        response_document = response.json()
        assert len(response_document['reviews']) == 3

        reviews.extend(ReviewFactory.create_batch(size=5, item=item))

        response = client.get(url + f"{item.id}/")
        assert response.status_code == 200
        response_document = response.json()
        assert len(response_document['reviews']) == 5
        for r, r_true in zip(response_document['reviews'], reversed(reviews[-5:])):
            assert(r['id'] == r_true.id)
