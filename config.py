import os

base_dir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'instance/projektai2.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

