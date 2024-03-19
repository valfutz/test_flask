from flask import Flask, render_template
from flask_login import LoginManager
from flask_migrate import Migrate

from app.api.views import api_views
from app.classes.views import ListView, DetailView
from app.database import db
from app.event.models import Event
from app.event.views import event_views
from app.main.views import main_views_login
from app.user.models import User
from app.user.views import user_views

app = Flask(__name__)

app.config.from_pyfile('config.py')

db.init_app(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# with app.app_context():
#     db.create_all()

app.register_blueprint(event_views)
app.register_blueprint(user_views)
app.register_blueprint(main_views_login)
app.register_blueprint(api_views)

menu = [{"name": "Home", "url": "/"},
        {"name": "Events", "url": "/events"},
        {"name": "Users", "url": "/users"},
        {"name": "API", "url": "/api"}, ]

app.jinja_env.globals.update(menu=menu)


@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(404)
def not_found_error(exc):
    return f"<h1>Looks like you're lost</h1>{exc}"


app.register_error_handler(404, not_found_error)

# @app.errorhandler(500)
# def internal_server_error(exc):
#     return f'<h1>My bad...</h1>{exc}'
#
#
# app.register_error_handler(500, internal_server_error)

app.add_url_rule("/class/users/",
                 view_func=ListView.as_view("user_list", User, "class/list.html"))
app.add_url_rule("/class/events/",
                 view_func=ListView.as_view("event_list", Event, "class/list.html"))

app.add_url_rule("/class/users/<int:id>",
                 view_func=DetailView.as_view("user_detail", User, "class/detail.html"))
app.add_url_rule("/class/events/<int:id>",
                 view_func=DetailView.as_view("event_detail", Event, "class/detail.html"))
