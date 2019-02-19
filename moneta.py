from app import app, db
from app.models import User, Post
from datetime import datetime


def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

