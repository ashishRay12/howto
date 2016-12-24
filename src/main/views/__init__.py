from .singleVid import *
from .moreVid import *

from main import app
singleVid = singleVid()




morevids = MoreVid()
app.add_route('/api/v1/moreVids', morevids)
app.add_route('/api/v1/vid/{id}', singleVid)
