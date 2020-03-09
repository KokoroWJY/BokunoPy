from mongoengine import connect, Document, EmbeddedDocument, \
    StringField, IntField, FloatField, ListField, EmbeddedDocumentField

connect('students')

SEX_CHOICES = (
    ('male', '男'),
    ('female', 'nv'),
)


class Grade(EmbeddedDocument):
    ''' 成绩 '''
    grade = StringField(required=True)
    score = FloatField(required=True)


class Student(Document):
    ''' 学生 '''
    name = StringField(max_length=32, required=True)
    age = IntField(required=True)
    grade = FloatField()
    sex = StringField(choices=SEX_CHOICES, required=True)
    address = StringField()
    grades = ListField(EmbeddedDocumentField(Grade))
