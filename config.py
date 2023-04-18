import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    """
    Set configuration variables for the flask app.
    Using environment variable where available
    otherwise create the config variable if not done
    already
    """

    SECRET_KEY = os.environ.get("SECRET_KEY") or "nana nana boo boo youll never guess"
    SQLACHEMY_DATA_URI =os.environ.get("DATABASE_URL") or "sqlite://" + os.path.join(basedir, 'app.db')
    SQLACHEMY_TRACK_MODIFICATIONS = False 