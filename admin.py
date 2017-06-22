#coding:utf-8
import tornado.web
from login import BaseHandler

class AdminHandler(BaseHandler):
     @tornado.web.authenticated
     def get(self):
        self.render('admin.html')

