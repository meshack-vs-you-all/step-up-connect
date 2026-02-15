from sqlalchemy import Column, Integer, String, Boolean, Float, Text, JSON, DateTime
from sqlalchemy.sql import func
from core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String, default="youth") # youth, mentor, admin
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    company = Column(String)
    location = Column(String)
    type = Column(String)
    description = Column(Text)
    salary = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Gig(Base):
    __tablename__ = "gigs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    budget = Column(Float)
    currency = Column(String, default="KES")
    is_premium = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Mentor(Base):
    __tablename__ = "mentors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    role = Column(String)
    company = Column(String)
    expertise = Column(JSON) # Storing list of strings as JSON
    availability = Column(String)
    image_url = Column(String, nullable=True)
