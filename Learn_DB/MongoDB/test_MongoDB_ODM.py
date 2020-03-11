from mongoengine import connect, Document, EmbeddedDocument, \
    StringField, IntField, FloatField, ListField, EmbeddedDocumentField

connect('students')

SEX_CHOICES = (
    ('male', '男'),
    ('female', '女'),
)


class Grade(EmbeddedDocument):
    ''' 成绩 '''
    name = StringField(required=True)
    score = FloatField(required=True)


class Student(Document):
    ''' 学生 '''
    name = StringField(max_length=32, required=True)
    age = IntField(required=True)
    grade = FloatField()
    sex = StringField(choices=SEX_CHOICES, required=True)
    address = StringField()
    grades = ListField(EmbeddedDocumentField(Grade), required=True)

    meta = {
        'collection': 'student',
        # 排序 "-"倒叙
        'ordering': ['-age']
    }


class TestMongoEngine(object):
    def add_one(self):
        ''' 添加一条数据 '''
        yuwen = Grade(name='语文', score=99)
        shuxue = Grade(name='数学', score=883)
        stu_obj = Student(name='hello', age=20, sex='female', grades=[yuwen, shuxue])
        stu_obj.remake = 'remake'
        stu_obj.save()
        return stu_obj

    def get_one(self):
        ''' 查找一条数据 '''
        return Student.objects.first()

    def get_more(self):
        ''' 查询多条数据 '''
        return Student.objects.all()

    def get_form_oid(self, oid):
        ''' 使用ID来获取数据 '''
        return Student.objects.filter(id=oid).first()

    def update(self):
        """ 修改(更新)数据 """
        # 修改所有男生的年龄增加10
        return Student.objects.filter(sex='male').update(inc__age=10)


def main():
    obj = TestMongoEngine()
    # rest = obj.add_one()
    # print(rest.pk)

    # rest = obj.get_one()
    # print(rest.id)
    # print(rest.name)

    # rows = obj.get_more()
    # for row in rows:
    #     print(row.name)

    # rest = obj.get_form_oid('5e6734c8a85e900657edc70c')
    # print(rest.id)
    # print(rest.name)


if __name__ == '__main__':
    main()
