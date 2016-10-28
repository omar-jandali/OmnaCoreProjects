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

