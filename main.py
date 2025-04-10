from sqlalchemy import create_engine, ForeignKey, Column, String, Integer,CHAR
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils.functions import database_exists
from flask import Flask, render_template, abort, url_for, request, redirect, session
# Use pip install -r requirements.txt to install modules

Base = declarative_base()

class Person(Base): 
    __tablename__ = "people"

    ssn = Column("ssn", Integer, primary_key=True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    gender = Column("gender", CHAR)
    age = Column("age", Integer)
    def __init__(self, ssn, first, last, gender, age):  
        self.ssn = ssn
        self.firstname = first
        self.lastname = last
        self.gender = gender
        self.age = age

    def __repr__(self):
        return f"({self.ssn}) {self.firstname} {self.lastname} ({self.gender}, {self.age})"

class Thing(Base):
    __tablename__ = "things"

    tid = Column("tid", Integer, primary_key=True)
    description = Column("description", String)
    owner = Column(Integer, ForeignKey("people.ssn"))

    def __init__(self, tid, description, owner):
        self.tid = tid
        self.description = description
        self.owner = owner

    def __repr__(self):
        return f"({self.tid}) {self.description} owned by {self.owner}"

db_url = "sqlite:///main.db" #variable for database URL
engine = create_engine(db_url, echo=True)

if database_exists(db_url):
    print("data base exists - carry on and do stuff") #in a real use case this would be you program just carrying on!
    Base.metadata.create_all(bind=engine) #create a new connection to the database and open a session
    Session = sessionmaker(bind=engine)
    session = Session()
    results=session.query(Thing, Person).filter(Thing.owner == Person.ssn).filter(Person.firstname == "Anna").all()
    for r in results:
        print(r)
else: #database does not exist so add some data
    print("database does not exist - so create it and add some data")
    Base.metadata.create_all(bind=engine)
  
    Session = sessionmaker(bind=engine)
    session = Session()

    p1 = Person(1, "Sallie", "Weiss", "F", 24)
    p2 = Person(2, "Henry", "Kemp", "M", 36)
    p3 = Person(3, "Harris", "Kemp", "M", 21)
    p4 = Person(4, "Ridwan", "Mcqrath", "M", 31)
    p5 = Person(5, "Honey", "Norton", "F", 47)

    t1 = Thing(1, "Keyboard", 5)
    t2 = Thing(2, "Mouse", 4)
    t3 = Thing(3, "Microphone", 3)
    t4 = Thing(4, "Monitor", 2)
    t5 = Thing(5, "Speaker", 1)
    t6 = Thing(6, "Desk Camera", 5)
    t7 = Thing(7, "Cellphone", 4)
    t8 = Thing(8, "Laptop", 3)
    t9 = Thing(9, "Docking Station", 2)
    t10 = Thing(10, "Headphones", 1)

    session.add(p1)
    session.add(p2)
    session.add(p3)
    session.add(p4)
    session.add(p5)
    session.add(t1)
    session.add(t2)
    session.add(t3)
    session.add(t4)
    session.add(t5)
    session.add(t6)
    session.add(t7)
    session.add(t8)
    session.add(t9)
    session.add(t10)
    session.commit()


