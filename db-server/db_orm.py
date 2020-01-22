from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import DateTime, func, or_
import datetime

from get_config import *
import json

db_data = config_json['config']['db_connection']

engine = create_engine(
    "postgresql+psycopg2://{0}:{1}@{2}/{3}".format( db_data['username'], 
                                                    db_data['pwd'],
                                                    db_data['host'], 
                                                    db_data['dbname']), echo=False)
meta = MetaData(bind=engine, schema=db_data['schema'], reflect=True)
meta.reflect(views=True)
Base = automap_base(metadata=meta)

class PollData(Base):
    __tablename__ = 'poll_data'
    __table_args__ = {'extend_existing': 'True'}

    id = Column(Integer, primary_key=True)
    # created_on = Column(DateTime, default=func.now())

class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': 'True'}

    id = Column(Integer, primary_key=True)

class PollAnswers(Base):
    __tablename__ = 'poll_answers'
    __table_args__ = {'extend_existing': 'True'}

    id = Column(Integer, primary_key=True)

class PollResultsView(Base):
    __tablename__ = 'poll_results_view'
    __table_args__ = {'extend_existing': 'True'}

    id = Column(Integer, primary_key=True)

Base.prepare()

Session = sessionmaker(bind=engine)

session = Session()

####################################

def orm_list(orm_list):
    new_list = []
    for rec in orm_list:
        new_list.append(orm_dict(rec))
    return new_list

def orm_dict(orm_dict):
    new_rec = {}
    for col in orm_dict.__table__.columns:
        orm_val = getattr(orm_dict, col.name)
        if type(orm_val) in [datetime.datetime, datetime.date, datetime.time]:
            new_rec[col.name] = str(orm_val)
        else :
            new_rec[col.name] = orm_val
    return new_rec