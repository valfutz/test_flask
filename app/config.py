import os
from dotenv import load_dotenv

load_dotenv()

DEBUG=True
PORT=5000

SECRET_KEY = os.environ['SECRET_KEY']
SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']
WTF_CSRF_ENABLED=os.environ['WTF_CSRF_ENABLED']