import app_config
import route_config
import database_config

from resources.vars.vars import app
from resources.vars.vars import db

db.create_all()
app.run(debug=True)
