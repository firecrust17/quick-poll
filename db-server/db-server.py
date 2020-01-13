# # from DCE.dbserver.flask_app import *
# from db_orm import *
# # from DCE.commons.config_reader import LgConfig

# import cherrypy
# # from paste.translogger import TransLogger
# # from moses_manager import *

# LC = LgConfig().getConfig()

# from DCE.dbserver.DCE_routes import *
# # from DCE.dbserver.raptor_routes import *
# import base64
# from DCE.dbserver.dce_resource import cipher_suite
# from DCE.service_handler.encrypt_string import decode_text, roles_secret_key
# from DCE.dbserver.flask_app import logger

# from DCE.dbserver.project_routes import *

# @app.before_request
# def print_op():
#     req_params = request.get_json()
#     # if req_params and req_params.get('hlc_roles_data'):
#     #     data = req_params['hlc_roles_data']
#     #     decoded_data = cipher_suite.decrypt(data.encode())
#     #     req_params['hlc_roles_data'] = decoded_data

# @app.teardown_appcontext
# def shutdown_session(exception=None):
#     logger.info("Removing session using app teardown.")
#     dbsession.remove()


# #Custom error handler if needed to throw exception on front end instead of handling internally.
# # @app.after_request
# # def handle_my_error(response):
# #     import json
# #     data = json.loads(response.get_data())
# #     if isinstance(data, dict) and data.get('errCode', -1) != 0:
# #         return make_response(json.dumps(data), 404)
# #     return response

# if __name__ == "__main__":

#     print ("Starting Application")

#     host = LC.get('DCESERVER', ).get('host')
#     port = int(LC.get('DCESERVER', ).get('port'))

#     server_type = LC.get('serverType', 'test')

#     server_private_key = LC.get('sslprivatekey', '')
#     server_ssl_cert = LC.get('sslcertificate', '')
#     server_ssl_cert_chain = LC.get('sslcertificatechain', '')

#     if server_type == 'test':
#         cherrypy_config = {'server.socket_host': host,
#                            'server.socket_port': port}
#     else:
#         cherrypy_config = {'server.socket_host': host,
#                            'server.socket_port': port,
#                            'server.ssl_module': "builtin",
#                            'server.ssl_private_key': server_private_key,
#                            'server.ssl_certificate': server_ssl_cert,
#                            'server.ssl_certificate_chain': server_ssl_cert_chain
#                            }

#     cherrypy.config.update(cherrypy_config)
#     app_log_enabled = TransLogger(app)
#     cherrypy.tree.graft(app_log_enabled, '/')

#     PATH = LC.get('PROJECTPATHS', ).get('Documents')
#     DOC_SERVE_PATH = LC.get('PROJECTPATHS').get('DownloadServeDir')

#     SERVICE_NAME = "download"


#     class Root(object):
#         pass


#     cherrypy.tree.mount(Root(), '/' + SERVICE_NAME + '/', config={
#         '/': {
#             'tools.staticdir.on': True,
#             'tools.staticdir.dir': DOC_SERVE_PATH
#         },
#     })

#     cherrypy.engine.start()
#     cherrypy.engine.block()


if __name__ == "__main__":

    # import psycopg2

    # conn = psycopg2.connect(database="poll-db", user = "postgres", password = "test", host = "127.0.0.1", port = "5432")

    # print ("Opened database successfully")
    

    from sqlalchemy import create_engine, MetaData
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.ext.automap import automap_base
    from sqlalchemy import Column, Integer, String
    from sqlalchemy.orm import sessionmaker


    db_data = {
        "username": "postgres",
        "pwd": "test",
        "host": "localhost",
        "dbname": "poll-db",
    }
    engine = create_engine("postgresql+psycopg2://{0}:{1}@{2}/{3}".format(db_data['username'], db_data['pwd'],
                                                                    db_data['host'], db_data['dbname']), echo=True)
    meta = MetaData(bind=engine, schema='current', reflect=False)
    Base = automap_base(metadata=meta)

    class PollData(Base):
        __tablename__ = 'poll_data'
        __table_args__ = {'extend_existing': 'True'}

        id = Column(Integer, primary_key=True)

    # print(PollData.__table__)
    # Session = sessionmaker(bind=engine)
    # print(Session)

    # session = Session()
    

    print(session.query(PollData).filter().all())


