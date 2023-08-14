from resources.vars.vars import app

from app.controllers.home_controller  import HomeController
from app.controllers.error_controller import ErrorController

app.add_route('GET', '/', HomeController().index, 'home_index')

app.add_error_route(404, ErrorController().error_404, '404_error')
