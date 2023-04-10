"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgpr1g5269v5rj89i9fg-a.oregon-postgres.render.com",
        database="demo_tx9h",
        user="demo_tx9h_user",
        password="LQWgNMmfQiVR706B6PkOayqj7hSorYnW")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
