from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

from get_config import *

db_data = config_json['config']['db_connection']

engine = create_engine(
    "postgresql+psycopg2://{0}:{1}@{2}/{3}".format( db_data['username'], 
                                                    db_data['pwd'],
                                                    db_data['host'], 
                                                    db_data['dbname']), echo=True)
meta = MetaData(bind=engine, schema=db_data['schema'], reflect=True)
Base = automap_base(metadata=meta)

class PollData(Base):
    __tablename__ = 'poll_data'
    __table_args__ = {'extend_existing': 'True'}

    id = Column(Integer, primary_key=True)

Base.prepare()

Session = sessionmaker(bind=engine)

session = Session()

