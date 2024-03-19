from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, render_template, request, jsonify, session, redirect
from app.actions.create_token import create_token
from app.event.models import Event
from app.user.models import User


api_views = Blueprint('api_views', __name__, url_prefix='/api')

menu1 = [{"name": "Home", "url": "/"},
         {"name": "API", "url": "/api"},
         {"name": "Events", "url": "/api/events"},
         {"name": "Users", "url": "/api/users"},
         {"name": "APILogin", "url": "/api/login"}, ]


@api_views.route('/')
def api_events():
    return render_template('api/api.html', title='api', menu=menu1)


@api_views.route('/login', methods=['POST', 'GET'])
def api_get_login():
    if 'username' not in session:
        return redirect('/login')
    if request.method == 'POST':
        password = session['password']
        username = session['username']
        hash = generate_password_hash('strong_password')
        if not check_password_hash(hash, password):
            return jsonify({'error': 'Invalid username or password'}), 401
        token = create_token(username)
        return jsonify({'token': token})
    return render_template('api/api_login.html', title='API/login', menu=menu1, a = session)


@api_views.route('/users', methods=['GET'])
def api_get_users_json():
    users = User.query.all()
    user_data = []

    for user in users:
        user_data.append({
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username,
            "password": user.password,
        })

    return jsonify(user_data)

@api_views.route('/events/', methods=['GET', 'POST'])
def api_get_events():
    events = Event.query.all()
    return render_template('api/api_events.html', title='API/events', menu=menu1,
                           events = events)

@api_views.route('/events/<int:event_id>/users', methods=['GET'])
def api_event_users(event_id):
    event = Event.query.get_or_404(event_id)
    users = User.query.filter_by(id=event.created_by).all()
    context = {
        'event': event,
        'event_users': users,
    }
    print(event.created_by)
    print(event.created_by)
    return render_template('api/event_users.html', title=f'API {event_id} users',
                           **context, menu=menu1)


@api_views.route('/events/json', methods=['GET'])
def api_get_events_json():
    events = Event.query.all()
    event_data = []

    for event in events:
        event_data.append({
            "id": event.id,
            "title": event.title,
            "description": event.description,
            "created_by": event.created_by,
            "begin_at": event.begin_at,
            "end_at": event.end_at,
            "max_users": event.max_users,
            "is_active": event.is_active,
        })

    return jsonify(event_data)

