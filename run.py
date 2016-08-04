import optparse
### File to run a local debug server
from fragforce import app

def flaskrun(app, default_host="0.0.0.0", default_port="8000"):
  parser = optparse.OptionParser()
  parser.add_option("-H", "--host",
          help="Hostname of the Flask app " + \
                  "[default %s]" % default_host, default=default_host)
  parser.add_option("-P", "--port",
          help="Port for the flask app " + \
                  "[default %s]" % default_port, default=default_port)
  parser.add_option("-d", "--debug",
          action="store_true", dest="debug",
          help=optparse.SUPPRESS_HELP)
  options, _ = parser.parse_args()
  app.run(debug=options.debug,
          host=options.host,
          port=int(options.port)
          )

flaskrun(app)
