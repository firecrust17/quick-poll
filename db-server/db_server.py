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
    
    server_type = config_json['config']['server_type']
    certificate_path = config_json['config']['certificates']

    if server_type == 'prod':
        cherrypy_config = {
            'server.socket_host': host,
            'server.socket_port': port,
            'server.ssl_module': "builtin",
            'server.ssl_private_key': certificate_path['private_key'],
            'server.ssl_certificate': certificate_path['certificate'],
            'server.ssl_certificate_chain': certificate_path['certificate_chain'],
        }
    else:
        cherrypy_config = {
            'server.socket_host': host,
            'server.socket_port': port,
        }


    cherrypy.config.update(cherrypy_config)
    
    app_log_enabled = TransLogger(app)
    cherrypy.tree.graft(app_log_enabled, '/')

    cherrypy.engine.start()
    cherrypy.engine.block()