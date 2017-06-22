#coding=utf-8

import tornado.web
from db import db_operation
from login import BaseHandler

def yanzheng(data,sucess,error):

    '根据数据库返回来的数据,来返回来alert的值'
    if data:
        suce =  '<script>\nalert ("%s")\nwindow.location.href="/manager_user"\n</script>'% sucess
        return suce
    else:
        err =  '<script>\nalert ("%s") \nwindow.location.href="/manager_user"\n</script>'% error
        return err


class ProjectHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.get_secure_cookie("username")
        select = db_operation().select('select * from project')
        self.render('project.html',select=select)

class DeployHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.get_secure_cookie("username")
        self.render('deploy.html')

    def post(self):
        pass
    # def post(self):
    #
    #     '新建用户'
    #
    #     username = self.get_argument('create_username')
    #     ms = self.get_argument('create_ms').encode('utf-8').decode('utf-8')
    #     password = self.get_argument('create_password','').decode('utf-8')
    #     create_admin = self.get_argument('create_admin',0)
    #     create_status = self.get_argument('create_status',0)
    #     # crypt_pass = pass_jm.pass_crypt(password)
    #     argument_data = {
    #           'username':username,
    #           'ms':ms,
    #           'password':password,
    #           'create_admin':create_admin,
    #           'create_status':create_status
    #     }
    #
    #     sql = 'insert into user (username,password,is_Admin,is_Lock,remaks)\
    #     values("%(username)s","%(password)s",%(create_admin)s,%(create_status)s,"%(ms)s")' % argument_data
    #
    #     select_name = db_operation().select('select username,password from user where username="%s"' % username)
    #     if select_name:
    #         message = yanzheng(0,'创建成功','创建失败,用户已存在')
    #         return self.write(message)
    #     else:
    #         data=db_operation().update(sql)
    #         # data = db_operation().select('select username,password from user where username="%s"' % username)
    #         message = yanzheng(data,'用户创建成功','用户创建失败')
    #         self.write(message)



