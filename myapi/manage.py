import click
from flask.cli import FlaskGroup

from myapi.app import create_app
from myapi.extensions import db
from myapi.models import User,UserType
from myapi.models.report import ReportType, Status

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

    goverment = UserType(
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

    
    # userTypes = UserType
    citizen_exist = db.session.query(db.exists().where(UserType.name == 'citizen')).scalar()
    if not citizen_exist:
        db.session.add(citizen)

    goverment_exist = db.session.query(db.exists().where(UserType.name == 'government')).scalar()
    if not goverment_exist:
        db.session.add(goverment)


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

    db.session.commit()
    click.echo("init data")


@cli.command("remove")
def remove():
    db.session.query(User).delete()
    db.session.commit()
    db.session.query(UserType).delete()
    db.session.commit()
    click.echo("deleted existing row ")

if __name__ == "__main__":
    cli()
