import click
from flask import Flask
from flask.cli import with_appcontext

from App.database import create_db, db
from App.main import app, migrate
from App.controllers import ( create_user, get_all_users_json )
import csv
from App.models import Job

@app.cli.command("init")
def initialize():
    create_db(app)
    with open('./jobs.csv') as f:
        jobs=csv.DictReader(f)

        for job in jobs:
            row=Job(name=job['name'], company=job['company'], email=job['email'], experience=job['experience'], details=job['details'])
            db.session.add(row)
        db.session.commit()

    print('database intialized')

@app.cli.command("create-user")
@click.argument("username")
@click.argument("password")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

@app.cli.command("get-users")
def get_users():
    print(get_all_users_json())