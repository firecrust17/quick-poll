from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

from get_config import *
import json

db_data = config_json['config']['db_connection']

engine = create_engine(
    "postgresql+psycopg2://{0}:{1}@{2}/{3}".format( db_data['username'], 
                                                    db_data['pwd'],
                                                    db_data['host'], 
                                                    db_data['dbname']), echo=False)
meta = MetaData(bind=engine, schema=db_data['schema'], reflect=True)
Base = automap_base(metadata=meta)

class PollData(Base):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': 'True'}

    id = Column(Integer, primary_key=True)

class User(Base):
    __tablename__ = 'poll_data'
    __table_args__ = {'extend_existing': 'True'}

    id = Column(Integer, primary_key=True)

class PollAnswers(Base):
    __tablename__ = 'poll_answers'
    __table_args__ = {'extend_existing': 'True'}

    id = Column(Integer, primary_key=True)

Base.prepare()

Session = sessionmaker(bind=engine)

session = Session()

####################################

from sqlalchemy.ext.declarative import DeclarativeMeta

class AlchemyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x not in ['classes', 'metadata', 'prepare']]:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)

def orm_list(orm_data):
    return json.loads(json.dumps(orm_data, cls=AlchemyEncoder))