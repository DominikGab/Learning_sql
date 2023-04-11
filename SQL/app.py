from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, Date, Float
import csv

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
   Column('station', String),
   Column('date', String),
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


with open('clean_stations.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        ins = clean_stations.insert().values(
            station=row['station'],
            latitude=float(row['latitude']),
            longitude=float(row['longitude']),
            elevation=float(row['elevation']),
            name=row['name'],
            country=row['country'],
            state=row['state']
        )
        engine.execute(ins)

with open('clean_measure.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        ins = clean_measure.insert().values(
            station=row['station'],
            date=row['date'],
            precip=float(row['precip']),
            tobs=int(row['tobs'])
        )
        engine.execute(ins)
