import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base #manipular las tablas de la bd


sqlite_file_name = '../database.sqlite'
base_dir = os.path.dirname(os.path.realpath(__file__))

database_url = f'sqlite:///{os.path.join(base_dir, sqlite_file_name)}'

# motor de la bd
# echo muestra por consola lo que se realiza
engine = create_engine(database_url, echo=True)

# crear sesion para conectarse a la bd
Session = sessionmaker(bind=engine)

Base = declarative_base()