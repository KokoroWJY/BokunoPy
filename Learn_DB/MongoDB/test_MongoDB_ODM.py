from mongoengine import connect, EmbeddedDocument, \
    StringField, IntField, FloatField, ListField, EmbeddedDocumentField, \
    DynamicDocument, Document

connect('students')

SEX_CHOICES = (
    ('male', '男'),
    ('female', '女'),
)


class Grade(EmbeddedDocument):
    ''' 成绩 '''
    name = StringField(required=True)
    score = FloatField(required=True)


# Document: 静态 严格按照这个模板, 要想新增属性需在模板上野新增类型
# DynamicDocument: 动态 要想新增属性可以直接写
class Student(DynamicDocument):
    ''' 学生 '''
    name = StringField(max_length=32, required=True)
    age = IntField(required=True)
    grade = FloatField()
    sex = StringField(choices=SEX_CHOICES, required=True)
    address = StringField()
    grades = ListField(EmbeddedDocumentField(Grade), required=True)
    # remake = StringField()

    meta = {
        'collection': 'student',  # 操作的数据库
        'ordering': ['-age']  # 排序 "-"倒叙
    }


class TestMongoEngine(object):
    def add_one(self):
        ''' 添加一条数据 '''
        yuwen = Grade(name='语文', score=99)
        shuxue = Grade(name='数学', score=883)
        stu_obj = Student(name='hello', age=20, sex='female', grades=[yuwen, shuxue])
        stu_obj.remake = 'remake'  # 增加新的属性
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

    def update_one(self):
        """ 修改(更新)一条数据 """
        return Student.objects.filter(sex='male').update_one(inc__age=100)

    def update_more(self):
        """ 修改(更新)多条数据 """
        # 修改所有男生的年龄增加10
        # $gt:大于
        # $lt:小于
        # $gte:大于或等于
        # $lte:小于或等于
        # age__gt=16: 选择年龄大于16岁的
        return Student.objects.filter(sex='male').update(inc__age=10)

    def delete(self):
        """ 删除数据 """
        # 删除一条数据
        # return Student.objects.filter(age=130).first().delete()

        # 删除多条数据
        return Student.objects.filter(sex='male').delete()


def main():
    obj = TestMongoEngine()
    rest = obj.add_one()
    print(rest.pk)

    # rest = obj.get_one()
    # print(rest.id)
    # print(rest.name)

    # rows = obj.get_more()
    # for row in rows:
    #     print(row.name)

    # rest = obj.get_form_oid('5e6734c8a85e900657edc70c')
    # print(rest.id)
    # print(rest.name)

    # rest = obj.update_one()
    # print(rest)

    # rest = obj.delete()
    # print(rest)


if __name__ == '__main__':
    main()
