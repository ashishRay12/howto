import falcon
from elasticsearch import Elasticsearch
import jinja2
import json
#tenjin.set_template_encoding('cp932')   # template encoding

class MoreVid():
    def on_get(self, req, resp, form={}, id=None):
        links = ["iNJdPyoqt8U","xDMP3i36naA","7AXosmNd3bw"]
        #fetch this video resource from elastic
        # templateLoader = jinja2.FileSystemLoader('main/templates')
        # templateEnv = jinja2.Environment( loader=templateLoader )
        # template = templateEnv.get_template( "singleVid.jinja" )
        #
        # templateVars = { "title" : "Test Example",
        # "video_link": 'https://www.youtube.com/embed/VxBzvziYAdk?showinfo=0&iv_load_policy=3&modestbranding=1&rel=0'}
        #
        # suggested_list = ["sr7JAiBLnhY",
        # "GdxBOpP1bIo",
        # "RPqHF9hy9ws",
        # "uYtUYt53H54","lDi9uFcD7XI","cw_cybkPy00"
        # ]
        # html = template.render( templateVars ,suggested=suggested_list)
        #
        # resp.content_type = 'text/html'
        resp.set_header ('Access-Control-Allow-Origin','http://localhost:8002')
        resp.body = json.dumps(links)
