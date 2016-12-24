import falcon
from .common import readForm

app = application = falcon.API(before=[readForm])
from .views import *
