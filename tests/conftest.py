import json
import pytest

from myapi.models import *
from myapi.app import create_app
from myapi.extensions import db as _db


@pytest.fixture
def app():
    app = create_app(testing=True)
    return app


@pytest.fixture
def db(app):
    _db.app = app

    with app.app_context():
        _db.create_all()

    yield _db

    _db.session.close()
    _db.drop_all()


@pytest.fixture
def admin_user(db):
    user = User(
        username='admin',
        email='admin@admin.com',
        password='admin'
    )

    db.session.add(user)
    db.session.commit()

    return user

@pytest.fixture
def citizen_user_type(db):
    citizen_type = UserType(name='citizen')
    db.session.add(citizen_type)
    db.session.commit()
    return citizen_type

@pytest.fixture
def government_user_type(db):
    government_type = UserType(name='government')
    db.session.add(government_type)
    db.session.commit()
    return government_type



@pytest.fixture
def citizen_user(db):
    prabowo = User(username='Prabowo',
                   email='prabowo@indonesia.go.id',
                   password='prabowo',
                   active=True,
                   user_type=citizen_user_type)

    db.session.add(prabowo)
    db.session.commit()
    return prabowo

@pytest.fixture
def government_user(db):
    prabowo = User(username='Jokowi',
                   email='jokowi@indonesia.go.id',
                   password='jokowi',
                   active=True,
                   user_type=government_user_type)

    db.session.add(prabowo)
    db.session.commit()
    return prabowo




@pytest.fixture
def admin_headers(admin_user, client):
    data = {
        'username': admin_user.username,
        'password': 'admin'
    }
    rep = client.post(
        '/auth/login',
        data=json.dumps(data),
        headers={'content-type': 'application/json'}
    )

    tokens = json.loads(rep.get_data(as_text=True))
    return {
        'content-type': 'application/json',
        'authorization': 'Bearer %s' % tokens['access_token']
    }


@pytest.fixture
def admin_refresh_headers(admin_user, client):
    data = {
        'username': admin_user.username,
        'password': 'admin'
    }
    rep = client.post(
        '/auth/login',
        data=json.dumps(data),
        headers={'content-type': 'application/json'}
    )

    tokens = json.loads(rep.get_data(as_text=True))
    return {
        'content-type': 'application/json',
        'authorization': 'Bearer %s' % tokens['refresh_token']
    }

@pytest.fixture
def citizen_user_headers(citizen_user, client):
    data = {
        'username': citizen_user.username,
        'password': 'prabowo'
    }
    rep = client.post(
        '/auth/login',
        data=json.dumps(data),
        headers={'content-type': 'application/json'}
    )

    tokens = json.loads(rep.get_data(as_text=True))
    return {
        'content-type': 'application/json',
        'authorization': 'Bearer %s' % tokens['access_token']
    }


@pytest.fixture
def government_user_headers(government_user, client):
    data = {
        'username': government_user.username,
        'password': 'jokowi'
    }
    rep = client.post(
        '/auth/login',
        data=json.dumps(data),
        headers={'content-type': 'application/json'}
    )

    tokens = json.loads(rep.get_data(as_text=True))
    return {
        'content-type': 'application/json',
        'authorization': 'Bearer %s' % tokens['access_token']
    }