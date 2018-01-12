# coding:utf8


from sqlalchemy import Column, String ,Integer, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, query, relationship
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("sqlite:///:memeory:", echo=True)
Base = declarative_base(engine)


class Parent(Base):
    __tablename__ = "parent"
    id = Column(Integer, primary_key=True)
    name = Column(String(10))

# 创建数据库表
Parent.metadata.create_all(engine)
# 运行后会在本地数据库创建一个数据库表




