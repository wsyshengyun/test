# coding:utf8


from sqlalchemy import Column, String ,Integer, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, query, relationship
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("sqlite:///:memeory:", echo=True)
Base = declarative_base(engine)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(10))
    password = Column(String(10))



    def __repr__(self):
        return "<User(id='%d', name='%s', password='%s')>" % (self.id, self.name, self.password)


# 创建数据库表
User.metadata.create_all(engine)
# 运行后会在本地数据库创建一个数据库表

#创建会话
Session = sessionmaker(bind=engine)
session = Session()

# 持久化实例对象
ed_user = User(id=1, name='xiexiaolu', password = 'dianwo')
Session.add(ed_user)
session.commit()


