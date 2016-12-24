from .singleVid import *
from main import app
singleVid = singleVid()

app.add_route('/api/v1/vid/{id}', singleVid)
