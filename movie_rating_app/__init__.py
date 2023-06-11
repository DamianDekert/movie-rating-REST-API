import os

from flask import Flask
from dotenv import load_dotenv


def create_app(db_url=None):

    app = Flask(__name__)
    load_dotenv()

    app.config['DATABASE_URL'] = os.getenv("DATABASE_URL")

    return app
