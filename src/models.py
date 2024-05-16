import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    apell = Column(String(250), nullable = False)
    accounts = Column(Integer, nullable = False)

    
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True)
    name = Column(String(50))
    email = Column(String(50), unique = True)
    password = Column(String(32))
    person_id = Column(Integer, ForeignKey('person.id'))
    person_id_relationship = relationship(Person)

class Planets(Base):
    __tablename__ = "planets"
    id = Column(Integer, primary_key = True)
    name = Column(String(50))
    population = Column(Integer)


class FavoritePlanets(Base):
    __tablename__ = "favorite_planets"
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_id_relationship =relationship(User)
    planets_id = Column(Integer,ForeignKey('planets.id'))
    planets_id_relationship = relationship(Planets)




class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
