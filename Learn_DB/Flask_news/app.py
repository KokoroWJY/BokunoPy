from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:68dxqiji@localhost:3306/new_test_flask?charset=utf8'
db = SQLAlchemy(app)


class News(db.Model):
    """" 创建数据表 """
    __tablename__ = 'news_test_flask'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.String(2000), nullable=False)
    types = db.Column(db.String(10), nullable=False)
    image = db.Column(db.String(300), nullable=True)
    auther = db.Column(db.String(20))  # 可以为空时可以不写  nullable=True
    view_count = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    is_valid = db.Column(db.Boolean)

    def __init__(self, title, content, types, image, auther, view_count, created_at, is_valid):
        self.title = title
        self.content = content
        self.types = types
        self.image = image
        self.auther = auther
        self.view_count = view_count
        self.created_at = created_at
        self.is_valid = is_valid

    def __repr__(self):
        return '<news_test_flask %r>' % self.title


# 运行News
# 从交互式 Python shell 中导入 db 对象并且调用
db.create_all()


@app.route('/wjy')
def hello_world():
    return 'Hello World! wjy'


if __name__ == '__main__':
    app.run()
