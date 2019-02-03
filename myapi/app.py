from flask import Flask

from myapi import auth, api
from myapi.extensions import db, jwt, migrate, celery

import logging
import os
from logging.handlers import RotatingFileHandler
# from myapi import config as _config


def create_app(config=None, testing=False, cli=False):
    """Application factory, used to create application
    """
    app = Flask('myapi')

    if not app.debug:
        # ...

        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/myapi.log', maxBytes=10240,
                                           backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('myapi startup')

    if not app.debug and not app.testing:
         ...

        # if app.config.LOG_TO_STDOUT:
        #     stream_handler = logging.StreamHandler()
        #     stream_handler.setLevel(logging.INFO)
        #     app.logger.addHandler(stream_handler)
        # else:
        #     if not os.path.exists('logs'):
        #         os.mkdir('logs')
        #     file_handler = RotatingFileHandler('logs/myapi.log',
        #                                        maxBytes=10240, backupCount=10)
        #     file_handler.setFormatter(logging.Formatter(
        #         '%(asctime)s %(levelname)s: %(message)s '
        #         '[in %(pathname)s:%(lineno)d]'))
        #     file_handler.setLevel(logging.INFO)
        #     app.logger.addHandler(file_handler)
        #
        # app.logger.setLevel(logging.INFO)
        # app.logger.info('myapi startup')

    configure_app(app, testing)
    configure_extensions(app, cli)
    register_blueprints(app)
    init_celery(app)

    return app


def configure_app(app, testing=False):
    """set configuration for application
    """
    # default configuration
    app.config.from_object('myapi.config')

    if testing is True:
        # override with testing config
        app.config.from_object('myapi.configtest')
    else:
        # override with env variable, fail silently if not set
        app.config.from_envvar("MYAPI_CONFIG", silent=True)


def configure_extensions(app, cli):
    """configure flask extensions
    """
    db.init_app(app)
    jwt.init_app(app)

    if cli is True:
        migrate.init_app(app, db)


def register_blueprints(app):
    """register all blueprints for application
    """
    app.register_blueprint(auth.views.blueprint)
    app.register_blueprint(api.views.blueprint)


def init_celery(app=None):
    app = app or create_app()
    celery.conf.broker_url = app.config['CELERY_BROKER_URL']
    celery.conf.result_backend = app.config['CELERY_RESULT_BACKEND']
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        """Make celery tasks work with Flask app context"""

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery
