from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean

# mysql://scott:tiger@loocalhost/foo 用户名: scott 密码: tiger 数据库名: foo
engine = create_engine('mysql://root:68dxqiji@localhost:3306/news?charset=utf8')  # 编码: charset
Base = declarative_base()

Session = sessionmaker(bind=engine)


class News(Base):
    """" 创建数据表 """
    __tablename__ = 'news_test'
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(String(2000), nullable=False)
    types = Column(String(10), nullable=False)
    image = Column(String(300), nullable=True)
    auther = Column(String(20))  # 可以为空时可以不写  nullable=True
    view_count = Column(Integer)
    created_at = Column(DateTime)
    is_valid = Column(Boolean)


# 运行News代码:
News.metadata.create_all(engine)


class ORM_test(object):
    def __init__(self):
        self.session = Session()

    def add_one(self):
        """ 新增一条数据 """
        new_obj = News(
            title="标题",
            content="内容",
            types="百家"
        )
        new_obj2 = News(
            title='title',
            content='content',
            types="tpyes"
        )
        self.session.add(new_obj)
        self.session.add(new_obj2)
        self.session.commit()
        return new_obj


def main():
    obj = ORM_test()
    rest = obj.add_one()
    print(rest.id)


if __name__ == '__main__':
    main()
