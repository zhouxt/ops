#coding=utf-8
import pass_jm
import tornado.web

from db import db_operation
from login import BaseHandler

def yanzheng(data,sucess,error):

    '根据数据库返回来的数据,来返回来alert的值'
    if data:
        suce =  '<script>\nalert ("%s")\nwindow.location.href="/manager_group"\n</script>'% sucess 
        return suce
    err =  '<script>\nalert ("%s") \nwindow.location.href="/manager_group"\n</script>'% error
    return err
     
class GroupHandler(BaseHandler):

    '管理组'

    @tornado.web.authenticated
    def get(self):

        self.get_secure_cookie("username")
        select = db_operation().select('select * from role')
        self.render('manager/group/manager_grp.html',select=select)

    def post(self):

        '新建组'
        create_grp  =  self.get_argument('create_grp').encode('utf-8').decode('utf-8')
        ms = self.get_argument('create_grp_ms').encode('utf-8').decode('utf-8')
        create_include_grp = self.get_argument('create_include_grp')

        argument_data = {
         
              'create_grp':create_grp,
              'ms':ms,
              'create_include_grp':create_include_grp
        }

        sql = 'insert into role (name,info,guser)\
        values("%(create_grp)s","%(ms)s","%(create_include_grp)s")' % argument_data
  
        select_name = db_operation().select('select name from role where name="%s"' % create_grp)
        if select_name:
            message = yanzheng(0,'创建成功','创建失败,组已存在')
            return self.write(message)
        else:
            data = db_operation().update(sql)
            message = yanzheng(data,'组创建成功','组创建失败')
            self.write(message)

class Edit_GroupHanler(BaseHandler):
    
    '编辑用户'

    @tornado.web.authenticated
    def post(self):
        
        id = self.get_argument('id')
        ms = self.get_argument('edit_grp_ms').encode('utf-8').decode('utf-8')
        edit_include_grp = self.get_argument('edit_include_grp')


        argument_data = {

              'id':id,
              'ms':ms,
              'edit_include_grp':edit_include_grp
        }

        sql = 'update role set \
        info="%(ms)s",guser="%(edit_include_grp)s" where id=%(id)s' % argument_data
        data = db_operation().update(sql)
        message = yanzheng(data,'用户修改成功','用户修改失败')
        self.write(message)

class Del_GroupHanler(BaseHandler):

    '删除用户'

    @tornado.web.authenticated
    def post(self):
     
        delete = self.get_argument('delete')
        sql = 'delete from role where id=%s' % delete
        data = db_operation().delete(sql)
        message = yanzheng(data,'组删除成功','组删除失败')
        self.write(message)

