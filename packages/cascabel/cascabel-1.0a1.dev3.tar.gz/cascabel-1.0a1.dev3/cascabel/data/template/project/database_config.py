from resources.vars.vars import db
from resources.vars.vars import app

db.add_database('main', f"sqlite:///{app.config['FOLDER']}/databases/main.db")