from Model import Model
from Field import *
from Database import Database

Model.db = Database('website.db')
Model.connection = Model.db.connect()

class Post(Model):
    title = CharField()
    body = TextField()
    created_at = DatatTime()
    published = BooleanField()

if __name__ == '__main__':
    pass
    # print(Post.get(1))
    # print(Post.find('title', 'LIKE', 'title 2'))
    # print(Post.all())