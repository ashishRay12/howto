import falcon
from elasticsearch import Elasticsearch
import jinja2
import json
#tenjin.set_template_encoding('cp932')   # template encoding

class singleVid():
    def on_get(self, req, resp, form={}, id=None):
        #fetch this video resource from elastic
        templateLoader = jinja2.FileSystemLoader('main/templates')
        templateEnv = jinja2.Environment( loader=templateLoader )
        template = templateEnv.get_template( "singleVid.jinja" )
        templateVars = { "title" : "Test Example",
        "video_link": "https://www.youtube.com/embed/VxBzvziYAdk?showinfo=0&iv_load_policy=3&modestbranding=1&rel=0"}
        
        Suggested = ["ICF0eAXpz3w","_bkX5VkZg8U","_oNNjHlKOxo","RGSXAn8L-_o","hepFlpCdTgU","ZkSXyfo6c-A"]
        html = template.render( templateVars,suggested=Suggested )
        resp.content_type = 'text/html'
        resp.body = html
