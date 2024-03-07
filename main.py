from flask import Flask, render_template, redirect, request, jsonify
from flask_security import auth_required, roles_accepted
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from api import api
from models import db, Theatre, Show
import config
from flask_security import Security
from sec import user_datastore
from flask_security.utils import hash_password
from redis import Redis
from celery import Celery
from celery.result import AsyncResult
from celery.schedules import crontab
from celery.result import AsyncResult
from celery.schedules import crontab
from models import User, Tickets, Theatre_Show, Theatre
from flask_login import current_user
from flask_caching import Cache
# from Cache import cache 
from flask_cors import CORS
from datetime import timedelta
import time


app=Flask(__name__)

app.config.from_object(config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

api.init_app(app)
db.init_app(app)   #sql alchemy instance
app.security=Security(app, user_datastore)
