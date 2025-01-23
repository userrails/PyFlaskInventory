import os

class Config:
    # Database configuration
    SQLALCHEMY_DATABASE_URI = 'postgresql://siv@localhost:5432/py_flask_inventory'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
