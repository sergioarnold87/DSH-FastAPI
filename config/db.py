from curses import meta
from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:root@localhost:3306/f1db")

meta_data = MetaData()