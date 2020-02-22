from flask import Flask, render_template
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


@app.route('/')
def index():
    '''新闻首页'''
    news_list = News.query.all()
    return render_template("index.html", news_list=news_list)


@app.route('/cat/<name>/')
def cat(name):
    '''新闻的类别'''
    news_list = News.query.filter(News.types == name)
    # 查询类别为 name 的新闻数据
    return render_template("cat.html", name=name, news_list=news_list)


@app.route('/detail/<int:pk>/')
def detail(pk):
    '''新闻详情信息'''
    new_obj = News.query.get(pk)
    return render_template("detail.html", new_obj=new_obj)


if __name__ == '__main__':
    app.run()
