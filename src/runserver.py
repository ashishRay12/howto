from main import app
from werkzeug.serving import run_simple

if __name__ == "__main__":
	from wsgiref.simple_server import make_server
	httpd = make_server('localhost', 8002, app)
	# Wait for a single request, serve it and quit.
	httpd.serve_forever()
