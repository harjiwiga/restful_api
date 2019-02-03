from myapi.models import User, Report


def user_factory(i):
    return User(
        username="user{}".format(i),
        email="user{}@mail.com".format(i)
    )

# def report_factory(i):
#     return Report(
#
#     )


