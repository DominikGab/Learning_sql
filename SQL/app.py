from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, Date, Float

engine = create_engine('sqlite:///C:\\Kodilla\\Kurs\\SQL\\air.db')

meta = MetaData()

clean_stations = Table(
   'clean_stations', meta,
   Column('station', String, primary_key=True),
   Column('latitude', Float),
   Column('longitude', Float),
   Column('elevation', Float),
   Column('name', String),
   Column('country', String),
   Column('state', String),
)

clean_measure = Table(
   'clean_measure', meta,
   Column('id', Integer, primary_key=True, autoincrement=True),
   Column('date', Date),
   Column('precip', Float),
   Column('tobs', Integer),
)

meta.create_all(engine)

engine = create_engine('sqlite:///C:\\Kodilla\\Kurs\\SQL\\air.db', echo=True)

print(engine.driver)

print(engine.table_names())

print(engine.execute("SELECT * FROM clean_stations"))

results = engine.execute("SELECT * FROM clean_stations")

for r in results:
   print(r)
