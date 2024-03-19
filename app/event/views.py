from flask import Blueprint, render_template, request, flash, redirect, url_for, abort, session
from sqlalchemy import extract

from app import db
from app.actions.login_required import login_required
from app.event.forms import EventForm, EventUpdateForm
from app.event.models import Event, EventUser
from app.user.models import User

event_views = Blueprint('e_views', __name__, url_prefix='/events')

menu_events = [{"name": "Home", "url": "/"},
               {"name": "Events", "url": "/events"},
               {"name": "Create", "url": "/events/create"}]


@event_views.route('/', methods=['GET'])
@login_required
def get_events():
    # events = Event.query.all()
    events = Event.query.filter(Event.created_by == session.get('username')).all()
    return render_template('event/list.html', title='Events', events=events,
                           menu=menu_events)


@event_views.route('/<int:id>', methods=['GET'])
def get_event_id(id):
    event = Event.query.get(id)
    return render_template('event/detail.html', title=f'Event {id}', event=event,
                           menu=menu_events)


@event_views.route('/create', methods=['GET', 'POST'])
def create_event():
    form = EventForm()
    if form.validate_on_submit():
        event = Event(title=form.title.data,
                      description=form.description.data,
                      created_by= session.get('username'),
                      max_users=form.max_users.data,
                      is_active=form.is_active.data)
        db.session.add(event)
        db.session.commit()
        flash('Event created successfully.', 'success')
        return redirect(url_for('e_views.get_event_id', id=event.id))
    return render_template('event/create.html', form=form, title='Event create',
                           menu=menu_events)

@event_views.route('/<int:id>/users', methods=['GET'])
def get_event_users(id):
    event = Event.query.get_or_404(id)
    event_users = EventUser.query.filter_by(event_id=id).all()
    users = [{'id': item.user_id,
              'username': User.query.get(item.user_id).username} for item in event_users]
    return render_template('event/event_users.html', title=f'Users for Event {id}',
                           users=users, event=event, menu=menu_events)



@event_views.route('/<int:id>/update', methods=['GET', 'POST'])
def update_event(id):
    global form
    event = Event.query.get_or_404(id)

    if request.method == 'GET':
        form = EventUpdateForm(obj=event)
        return render_template('event/update.html', title=f'Event {id} update',
                               form=form, event=event)

    if request.method == 'POST':
        form = EventUpdateForm()
        if form.validate_on_submit():
            form.populate_obj(event)
            db.session.add(event)
            db.session.commit()
            return redirect(url_for('e_views.get_event_id', id=id))
    return render_template('event/update.html', form=form, event=event)
