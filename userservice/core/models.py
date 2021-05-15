import os

from sqlalchemy import (
    Column,
    String,
    Integer,
    create_engine,
    ForeignKey,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()
engine = create_engine(os.environ.get("PSQL_URL"))

Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    login = Column(String(100), nullable=False)
    password_hash = Column(String(255), nullable=False)
    telegram = Column(String(100))
    files = relationship("File", back_populates="files")


class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    size = Column(Integer, nullable=False)
    status = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
