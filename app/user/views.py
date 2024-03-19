from flask import Blueprint, render_template, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

from app import db
from app.actions.login_required import login_required
from app.user.forms import UserForm
from app.user.models import User

user_views = Blueprint('user_views', __name__, url_prefix='/users/')

menu_users = [{"name": "Home", "url": "/"},
        {"name": "Users", "url": "/users"},
        {"name": "Login", "url": "/login"},
        {"name": "Sign up", "url": "/users/register"},]


@user_views.route('/', methods=['GET'])
@login_required
def get_users():
    users = User.query.all()
    context = {
        'users': users,
    }
    return render_template('user/list.html', title='Users', **context,
                           menu=menu_users)

@user_views.route('/register', methods=['GET', 'POST'])
def register():
    form = UserForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user:
            flash('This username is already taken. Please choose another one.', 'error')
            return redirect(url_for('user_views.register'))

        hash = generate_password_hash(form.psw.data)

        new_user = User(first_name=form.first_name.data,
                        last_name=form.last_name.data,
                        username=form.username.data,
                        password=hash)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login_views.get_login'))
    else:
        for error in form.errors.values():
            flash(error, 'error')
        return render_template('user/register.html', title='Sign Up', form=form,
                           menu=menu_users)