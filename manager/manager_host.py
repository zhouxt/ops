#coding:utf-8
import pass_jm
import tornado.web


from db import db_operation
from login import BaseHandler

def yanzheng(data,sucess,error):

    '根据数据库返回来的数据,来返回来alert的值'
    if data:
        suce =  '<script>\nalert ("%s")\nwindow.location.href="/manager_host"\n</script>'% sucess
        return suce
    else:
        err =  '<script>\nalert ("%s") \nwindow.location.href="/manager_host"\n</script>'% error
        return err


class HostHandler(BaseHandler):

    '管理主机'

    @tornado.web.authenticated
    def get(self):
    	self.get_secure_cookie("username")
    	select = db_operation().select('select * from server')
        self.render('manager/host/manager_host.html',select=select)

    def post(self):

    	'新建主机'

    	hostname = self.get_argument('create_hostname')
    	hostip = self.get_argument('create_ip')
    	os = self.get_argument('create_os')
    	cpuinfo = self.get_argument('create_cpuinfo')
    	meminfo = self.get_argument('create_meminfo')
        diskinfo = self.get_argument('create_diskinfo')
    	statusinfo = self.get_argument('create_statusinfo')
        argument_data = {
              'hostname':hostname,
              'hostip':hostip,
              'os':os,
              'cpuinfo':cpuinfo,
              'meminfo':meminfo,
              'diskinfo':diskinfo,
              'statusinfo':statusinfo
        }
        sql = 'insert into server (hostname,ip,os,server_cpu,server_mem,server_disk,vm_status)\
        values("%(hostname)s","%(hostip)s","%(os)s","%(cpuinfo)s","%(meminfo)s","%(diskinfo)s","%(statusinfo)s")' % argument_data
        select_name = db_operation().select('select hostname,ip from server where ip="%s"' % hostip)
        if select_name:
            message = yanzheng(0,'创建成功','创建失败,主机已存在')
            return self.write(message)
        else:
            data = db_operation().update(sql)
            message = yanzheng(data,'主机创建成功','主机创建失败')
            self.write(message)

class Edit_HostHandler(BaseHandler):
    
    '编辑主机'

    @tornado.web.authenticated
    def post(self):
        id = self.get_argument('id')
        hostname = self.get_argument('hostname')
        ip = self.get_argument('ip')
        os = self.get_argument('os')
        cpu = self.get_argument('cpu')
        mem = self.get_argument('mem')
        disk = self.get_argument("disk")
        status = self.get_argument("status",0)
        argument_data = {
            'id':id,
            'hostname':hostname,
            'ip':ip,
            'os':os,
            'cpu':cpu,
            'mem':mem,
            'disk':disk,
            'status':status
        }
        sql = 'update server set hostname="%(hostname)s",ip="%(ip)s",os="%(os)s",server_cpu="%(cpu)s",server_mem="%(mem)s",server_disk="%(disk)s",vm_status="%(status)s" where id="%(id)s"' % argument_data
        data = db_operation().update(sql)
        message = yanzheng(data,'主机修改成功','主机修改失败')
        self.write(message)

class Del_HostHandler(BaseHandler):

    '删除主机'

    @tornado.web.authenticated
    def post(self):
        delete = self.get_argument('delete')
        sql = 'delete from server where id=%s' % delete
        data = db_operation().delete(sql)
        message = yanzheng(data,'主机删除成功','主机删除失败')
        self.write(message)
