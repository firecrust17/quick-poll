from db_api import *    # config_json imported here
from paste.translogger import TransLogger
import cherrypy

if __name__ == "__main__":

    host = config_json['config']['db_server']['host']
    port = int(config_json['config']['db_server']['port'])

    cherrypy_config = {
        'server.socket_host': host,
        'server.socket_port': port
    }

    cherrypy.config.update(cherrypy_config)
    
    app_log_enabled = TransLogger(app)
    cherrypy.tree.graft(app_log_enabled, '/')

    cherrypy.engine.start()
    cherrypy.engine.block()