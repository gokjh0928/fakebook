import os
from dotenv import load_dotenv

basedir = os.path.dirname(__name__)
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    # The SECRET_KEY is in the .env file
    SECRET_KEY = os.getenv('SECRET_KEY')
    FLASK_APP = os.getenv('FLASK_APP')
    FLASK_ENV = os.getenv('FLASK_ENV')
