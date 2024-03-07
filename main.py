from flask import Flask, render_template, redirect, request, jsonify
from flask_security import auth_required, roles_accepted
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from api import api
# from models import db, Theatre, Show
import config
from flask_security import Security
from sec import user_datastore
from flask_security.utils import hash_password
# from redis import Redis
# from celery import Celery
# from celery.result import AsyncResult
# from celery.schedules import crontab
# from celery.result import AsyncResult
# from celery.schedules import crontab
# from models import User, Tickets, Theatre_Show, Theatre
# from flask_login import current_user
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


# redis = Redis(host='localhost', port=6379)


# app.config.update(
#     CELERY_BROKER_URL='redis://localhost:6379/0',
#     RESULT_BACKEND='redis://localhost:6379/0'
# )


# from celery_config import make_celery
# celery = make_celery(app)

from cache import initialize_cache
initialize_cache(app)

CORS(app)




# @app.route("/gen_csv/<string:t_s>/<int:id>")
# # @auth_required('token')
# def gen_csv(t_s,id):
#     task=generate_csv_specific.delay(t_s,id)
#     return jsonify({"task_id":task.id})


# @app.route('/status/<string:task_id>')
# def get_download_status(task_id,app = celery):
#     # Check the Celery task status using the task ID
#     res = AsyncResult(task_id)
#     status = res.state
#     return jsonify({"status":status})
    



@app.get("/")
def home():
    return render_template("index.html")


with app.app_context():
    if not app.config['INIT_SETUP']:
        # db.create_all()
        # # user_datastore.create_role(name="admin", description="Admin - can create/delete/edit shows and theatres")
        # # user_datastore.create_role(name='user', description="Can book shows/ provide rating")
        # if not user_datastore.find_user(email="admin@gmail.com"):
        #     user_datastore.create_user(username="admin", email="admin@gmail.com", password=hash_password("1234"), roles=["admin"])

        # db.session.commit()
        app.config.update(INIT_SETUP=True)


if __name__=="__main__":
    app.run(debug=True)
    
