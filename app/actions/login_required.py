from flask import redirect, url_for, session

def login_required(route_func):
    def wrapper(*args, **kwargs):
        if 'username' not in session:
            return redirect('/login')
        return route_func(*args, **kwargs)
    return wrapper
