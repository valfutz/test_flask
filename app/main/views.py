from flask import Blueprint, render_template, request, session, redirect, url_for, flash

from werkzeug.security import check_password_hash

from app.main.forms import LoginForm
from app.user.models import User

main_views_login = Blueprint('login_views', __name__, url_prefix='/login/')

menu_main = [{"name": "Home", "url": "/"},
             {"name": "Logout", "url": "/login/logout"}, ]


@main_views_login.route('/', methods=['GET', 'POST'])
def get_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None:
            if user and check_password_hash(user.password, form.password.data):
                session['username'] = request.form['username']
                return redirect('/events')
            else:
                flash('Invalid username or password', 'error')
        else:
            return redirect(url_for('user_views.register'))

    return render_template('main/login.html', title='Login', form=form, menu=menu_main)


@main_views_login.route('/logout')
def get_logout():
    if 'username' in session:
        session.pop('username', None)
        session.pop('password', None)
    return redirect('/login')
