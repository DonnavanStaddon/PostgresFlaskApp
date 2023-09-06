from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from our localhost "chinook" db
db = create_engine("postgresql://postgres:PASSWORD@localhost:5432/chinook")
base = declarative_base()

# crate table
class Programmer(base):
    __tablename__="Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)

# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declaritive_base subclass
base.metadata.create_all(db)

# create data for db
ada_lovelace = Programmer(
    first_name = "Ada",
    last_name = "Lovelave",
    gender = "F",
    nationality = "British", 
    famous_for = "First Programmer"
)

# create data for db
alan_turing = Programmer(
    first_name = "Alan",
    last_name = "Turing",
    gender = "M",
    nationality = "British", 
    famous_for = "Modern Computing"
)

# create data for db
grace_hopper = Programmer(
    first_name = "Grace",
    last_name = "Hopper",
    gender = "F",
    nationality = "American", 
    famous_for = "COBOL language"
)

# create data for db
margaret_hamilton = Programmer(
    first_name = "Margaret",
    last_name = "Hamilton",
    gender = "F",
    nationality = "American", 
    famous_for = "Apollo 11"
)

# create data for db
bill_gates = Programmer(
    first_name = "Bill",
    last_name = "Gates",
    gender = "M",
    nationality = "American", 
    famous_for = "Microsoft"
)

# create data for db
tim_berners_lee = Programmer(
    first_name = "Tim",
    last_name = "Berners-Lee",
    gender = "M",
    nationality = "British", 
    famous_for = "World Wide Web"
)

# create data for db
donnavan_staddon = Programmer(
    first_name = "Donnavan",
    last_name = "Staddon",
    gender = "M",
    nationality = "British", 
    famous_for = "Fullstack Website Developer"
)

# add data to db
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
session.add(donnavan_staddon)

# insert data into bd
session.commit()

# view/query data in Programmer Table
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )