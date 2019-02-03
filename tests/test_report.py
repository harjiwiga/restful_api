import factory
from pytest_factoryboy import register
from myapi.models import Report, ReportType


# def test_create_report(client, db, citizen_header):
#     # test bad data
#     data = {
#         'username': 'created'
#     }
#     rep = client.post(
#         '/api/v1/reports',
#         json=data,
#         headers=citizen_header
#     )
#     assert rep.status_code == 422
#
#     data['password'] = 'admin'
#     data['email'] = 'create@mail.com'
#
#     rep = client.post(
#         '/api/v1/users',
#         json=data,
#         headers=citizen_header
#     )
#     assert rep.status_code == 201
#
#     data = rep.get_json()
#     user = db.session.query(Report).filter_by(id=data['user']['id']).first()
#
#     assert user.username == 'created'
#     assert user.email == 'create@mail.com'


def test_get_all_report_type(client, db, citizen_user_headers):
    broken_road = ReportType(
        name='broken_road'
    )

    traffic_jam = ReportType(
        name='traffic_jam'
    )

    wild_animal = ReportType(
        name='wild_animal'
    )

    flood = ReportType(
        name='flood'
    )

    db.session.add_all([broken_road, traffic_jam, wild_animal, flood])
    db.session.commit()

    rep = client.get('/api/v1/report/types', headers=citizen_user_headers)
    assert rep.status_code == 200
