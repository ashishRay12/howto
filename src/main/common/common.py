import falcon
import json
from falcon.util.uri import parse_query_string
from cStringIO import StringIO
from werkzeug.http import parse_options_header
from werkzeug.formparser import parse_form_data

def readForm(req,resp,params):
    form = dict()
    files = dict()
    if req.method == "GET":
        form = parse_query_string(req.query_string)
        params["form"] = form
    else:
        if 'json' in req.get_header('content-type', None):
            form = json.load(req.stream)
            params['form'], params['files'] = dict(form), dict(files)
        else:
            mimetype, options = parse_options_header(req.get_header('content-type'))
            data = req.stream.read()
            environ = {'wsgi.input': StringIO(data),
                       'CONTENT_LENGTH': str(len(data)),
                       'CONTENT_TYPE': req.get_header('content-type'),
                       'REQUEST_METHOD': 'POST'}
            stream, tempform, tempfiles = parse_form_data(environ)
            for item in tempform:
                form[item] = tempform[item]
            di = parse_query_string(req.query_string)
            for item in di:
                form[item] = di[item]
            for item in tempfiles:
                files[item] = tempfiles[item]
            if files:
                params['files'] = dict(files)
            params['form'] = dict(form)
