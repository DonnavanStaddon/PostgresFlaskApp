from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from our localhost "chinook" db
db = create_engine("postgresql://postgres:litStunt01@localhost:5432/chinook")
base = declarative_base()


# create a class-based model for the "Artist" table
class Artist(base):
    __table__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)


# create a class-baased model for the "Album" table
class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))


# create a class-based model for the "Track table
class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.ArtistId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()


# creating the database using declaritive_base subclass
base.metadata.create_all(db)


# Query 1 - select all records from the "Artist" table
artists = session.query(Artist)
for artist in artists:
    print(artist.ArtistId, artist.Name, sep=" | ")