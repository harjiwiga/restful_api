import click
from flask.cli import FlaskGroup

from myapi.app import create_app
from myapi.extensions import db
from myapi.models import User, UserType, Role
from myapi.models.report import ReportType, Status, Report
from myapi.models import helpers
from myapi.models.blacklist import TokenBlacklist


def create_myapi(info):
    return create_app(cli=True)


@click.group(cls=FlaskGroup, create_app=create_myapi)
def cli():
    """Main entry point"""


@cli.command("init")
def init():
    """Init application, create database tables
    and create a new user named admin with password admin
    """

    click.echo("create database")
    db.create_all()
    click.echo("done")

    click.echo("create user")

    admin_exsist = db.session.query(db.exists().where(User.username == 'admin')).scalar()

    user = User(
        username='admin',
        email='admin@mail.com',
        password='admin',
        active=True
    )

    citizen = UserType(
        name='citizen'
    )

    government = UserType(
        name='government'
    )


    traffic_accident = ReportType(
        name='traffic_accident'
    )

    broken_road = ReportType(
        name='broken_road'
    )

    wild_animal = ReportType(
        name='wild_animal'
    )

    # ============== init role ================
    helpers.get_or_create(
        db.session,
        Role,
        name='admin'
    )

    helpers.get_or_create(
        db.session,
        Role,
        name='government'
    )

    helpers.get_or_create(
        db.session,
        Role,
        name='citizen'
    )

    helpers.get_or_create(
        db.session,
        Role,
        name='anonymous'
    )
    # =========================================


    # userTypes = UserType
    citizen_exist = db.session.query(db.exists().where(UserType.name == 'citizen')).scalar()
    if not citizen_exist:
        db.session.add(citizen)

    goverment_exist = db.session.query(db.exists().where(UserType.name == 'government')).scalar()
    if not goverment_exist:
        db.session.add(government)

    if not admin_exsist:
        db.session.add(user)

    accident_exist = db.session.query(db.exists().where(ReportType.name == 'traffic_accident')).scalar()
    if not accident_exist:
        db.session.add(traffic_accident)

    broken_road_exist = db.session.query(db.exists().where(ReportType.name == 'broken_road')).scalar()
    if not broken_road_exist:
        db.session.add(broken_road)

    wild_animal_exist = db.session.query(db.exists().where(ReportType.name == 'wild_animal')).scalar()
    if not wild_animal_exist:
        db.session.add(wild_animal)

    reported = Status(name= 'reported')
    on_handled = Status(name='on_handled')
    done = Status(name='done')

    reported_exist = db.session.query(db.exists().where(Status.name == 'reported')).scalar()
    if not reported_exist:
        db.session.add(reported)

    on_handled_exist = db.session.query(db.exists().where(Status.name == 'on_handled')).scalar()
    if not on_handled_exist:
        db.session.add(on_handled)

    done_exist = db.session.query(db.exists().where(Status.name == 'done')).scalar()
    if not done_exist:
        db.session.add(done)
    db.session.flush()
    government = UserType.query.filter_by(name='government').first()
    jokowi = User(username='Jokowi',
                        email='jokowi@indonesia.go.id',
                        password='jokowi',
                        active =True,
                        user_type = government
                  )

    jokowi_exist = db.session.query(db.exists().where(User.username == 'Jokowi')).scalar()

    if not jokowi_exist:
        db.session.add(jokowi)

    citizen = UserType.query.filter_by(name='citizen').first()
    prabowo = User(username='Prabowo',
                  email='prabowo@indonesia.go.id',
                  password='prabowo',
                  active=True,
                  user_type=citizen)

    prabowo_exist = db.session.query(db.exists().where(User.username == 'Prabowo')).scalar()

    if not jokowi_exist:
        db.session.add(jokowi)

    if not prabowo_exist:
        db.session.add(prabowo)



    maruf_amin = User(
        username = 'Maruf Amin',
        email = 'maruf.amin@indonesia.go.id',
        password = 'maruf',
        active = True,
        user_type = citizen
    )

    maruf_exist = db.session.query(db.exists().where(User.email == 'maruf.amin@indonesia.go.id')).scalar()
    if not maruf_exist:
        db.session.add(maruf_amin)

    # helpers.get_or_create(
    #     db.session,
    #     User,
    #     username='Maruf Amin',
    #     email = 'maruf.amin@indonesia.go.id',
    #     password = 'maruf',
    #     active = True,
    #     user_type= citizen
    # )




    db.session.commit()
    click.echo("init data")


@cli.command("clear")
def clear():
    db.session.query(TokenBlacklist).delete()
    db.session.commit()

    db.session.query(User).delete()
    db.session.commit()

    db.session.query(UserType).delete()
    db.session.commit()

    db.session.query(UserType).delete()
    db.session.commit()

    db.session.query(Status).delete()
    db.session.commit()

    db.session.query(Report).delete()
    db.session.commit()

    db.session.query(ReportType).delete()
    db.session.commit()

    click.echo("deleted existing row ")

if __name__ == "__main__":
    cli()
