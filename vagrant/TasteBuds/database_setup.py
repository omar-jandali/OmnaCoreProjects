"""

The following file is the sole property of OmnaCore Consolidate and is strickly used for
the development of OmnaCores Tastebuds Web Application

File and code usage is limited to the consent of OmnaCore.

You may email Omnar Jandali at omarjandali@omnacore.com for inqueries

"""

"""
This is the database setup file which will be used to create every single database layout,
  structure, and column description that will be used in this web app.

  The initial tables include:
    Restaurants: store restaurants name and id
    Restaurants Info: this will store all of the general restaurant information
    Restaurants Rating: this will include all of the ratings that are given to all
      of the restuarants by users

    Dishes: This will store all of the dishes id and name that are given
    Dishes Info: this will store general information about the dishes added
    Dishes Ratings: this will include the ratings that are given to dishes by users

"""

# the following are all of the files that need to be imported
import os
import sys
from sqlalchemy import Column, String, Integer, ForeignKey, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

# the following sets the Base as the declarative_base
Base = declarative_base()

class Restaurants(Base):
  __tablename__ = 'restaurants'

  id = Column(Integer, primary_key = True)
  name = Column(String(200), nullable = False, unique = True, index = True)

class Restaurants_Location(Base):
  __tablename__ = 'restaurants_location'

  street = Column(String(220), nullable = False)
  city = Column(String(100), nullable = False, index = True)
  state = Column(String(5), nullabe = False)
  zip = Column(Integer(5), nullable = False)
  restaurants_id = Column(Integer(100), ForeignKey('restaurants.id'))
  restaurants = relationship(Restaurants)

class Restaurants_Info(Base):
  __tablename__ = 'restaurants_info'

  cuisine = Column(String(100), nullable = False, index = True)
  pricing = Column(String(100), nullable = False)
  dining = Column(String(100), nullable = False)
  hours = Column(String(100), nullable = False)
  restaurants_id = Column(Integer(100), ForeignKey('restaurants.id'))
  restaurants = relationship(Restaurants)

class Restaurants_Rating(Base):
    __tablename__ = 'restaurants_rating'

    food = Column(String(100), nullable = True)
    service = Column(String(100), nullable = True)
    pricing = Column(String(100), nullable = True)
    location = Column(String(100), nullable = True)
    access = Column(String(100), nullable = True)
    restaurants_id = Column(Integer(100), ForeignKey('restaurants.id'))
    restaurants = relationship(Restaurants)