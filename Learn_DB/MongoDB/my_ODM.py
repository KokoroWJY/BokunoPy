from mongoengine import *
from datetime import datetime

connect('students')

SEX = {
    ('male', '男'),
    ('female', '女')
}


class Grade(EmbeddedDocument):
    name = StringField(required=True)
    score = FloatField(required=True)


class Students(Document):
    name = StringField(max_length=10, required=True)
    age = IntField(max_value=200, required=True)
    sex = StringField(choices=SEX, required=True)
    grade = ListField(EmbeddedDocumentField(Grade), required=True)
    date = DateField()


class Add(object):
    def add(self):
        English = Grade(name='英语', score=100)
        Chinese = Grade(name='语文', score=90)
        Match = Grade(name='数学', score=70)
        student = Students(name='tsy', age=20, sex='female', grade=[English, Chinese, Match])
        student.save()
        return student


def main():
    Add().add()


if __name__ == '__main__':
    main()
