import requests


def put():
    r = requests.put('http://127.0.0.1:5000/put_review/1',
                     json={'title': 'TEST tile',
                     'review': 'TEST Review'}
                     )
    print(r.status_code)
    print(r.text)


put()
