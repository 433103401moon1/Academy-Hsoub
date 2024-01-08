from datetime import datetime
import json
from http.server import SimpleHTTPRequestHandler, HTTPServer
from Model import Model
from Field import *
from Database import Database
from urllib.parse import urlparse, parse_qs


Model.db = Database('website.db')
Model.connection = Model.db.connect()

class Post(Model):
    title = CharField()
    body = TextField()
    created_at = DatatTime()
    published = BooleanField()

if __name__ == '__main__':
    class MyHandler(SimpleHTTPRequestHandler):
        def do_GET(self):
            if self.path == '/':
                return SimpleHTTPRequestHandler.do_GET(self)
            
            elif self.path == '/posts':
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(Post.all()).encode('utf-8'))
            else:
                id_post = int(self.path.split('/')[-1])
                result = Post.get(id_post)
                if result is False:
                    self.send_response(404)
                    self.send_header('Content-type', 'text/plain')
                    self.end_headers()
                    self.wfile.write(b'Not Foud')
                    return
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(Post.get(id_post)).encode('utf-8'))   
            # بنيته من نفسي قبل مشاهدة الحل
            # if self.path == '/posts/1' or self.path == '/posts/2':
            #     self.send_response(200)
            #     self.send_header('Content-Type', 'application/json')
            #     self.end_headers()
            #     self.wfile.write(json.dumps(Post.get(int(self.path[-1]))).encode('utf-8'))

        def do_POST(self):
            length = int(self.headers.get('content-length'))
            print("length: ", length)
            body = self.rfile.read(length)
            print("body: ", body)
            string = urlparse(body)
            print("string: ", string)
            post = parse_qs(string.path.decode('utf-8'))
            print("post: ", post)
            Post.create(title=post['title'][0], body=post['body'][0], created_at=datetime.now(), published=True)
            self.send_response(301)
            self.send_header('location', 'localhost:8001')
            self.end_headers()


    # ("", 8001) >> ( "عنوان الاي بي - اذا فارغ افتراضيlocalhost ", رقم المنفذ انت حر في اختياره)
    # SimpleHTTPRequestHandler >> مسؤول عن ادارة طلبات السيرفر
    # with نفذ الكود في حال عدم وجود اخطاء
    # as اسم مستعار للتسهيل
    with HTTPServer(("", 8001), MyHandler ) as server: 
        print("server running")
        server.serve_forever()