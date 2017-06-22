#coding:utf-8
import pymysql
config = {
         'host':'192.168.101.160',
         'port':3306,
         'user':'zxt',
         'password':'password',
         'db':'zxt_cmdb',
         'charset':'utf8'
         }


class db_operation(object):
    'MySQL的增删改查'
    def __init__(self):
        try:
            self.connect_db()
        except:
            print '数据库连接失败!'
    def connect_db(self):
        self.db=pymysql.connect(**config)
        self.cur=self.db.cursor()

    def close_db(self):
        self.cur.close()
        self.db.close()

    def select(self,sql):
        try:
            self.cur.execute(sql)
            select_result = self.cur.fetchall()
            self.db.commit()
            return select_result
        except:
            self.close_db()
            print 'SQL 语法有问题!'

    def update(self,sql):
        try:
            self.cur.execute(sql)
            # update_result = self.cur.fetchone()
            self.db.commit()
            return 1
            # return update_result
        except:
            self.close_db()
            print 'SQL 语法有问题!'
            return 0

    def delete(self,sql):
        try:
            self.cur.execute(sql)
            # delete_result = self.cur.fetchone()
            self.db.commit()
            return 1
        except:
            self.close_db()
            print 'SQL 语法有问题!'
            return 0







     #        self.sql = sql
     #        self.db = db
     #    except Exception,e:
     #        print '数据库连接失败!'
    #
    # def select(self):
     #    try:
     #        select_data = self.db.execute(self.sql)
     #        return select_data
     #    except Exception,e:
     #        print self.sql
     #        print 'SQL 语法有问题!'
     #    finally:
     #        self.db.close()
    #
    # def update(self):
     #    try:
     #        update_data = self.db.execute(self.sql)
     #        return update_data
     #    except Exception,e:
     #        print self.sql
	#     print 'SQL 语法有问题!'
	# finally:
	#     self.db.close()
    #
    # def delete(self):
     #    try:
	#     delete_data = self.db.execute(self.sql)
	#     return delete_data
	# except Exception,e:
	#     print self.sql
	#     print 'SQL 语法有问题!'
	# finally:
	#     self.db.close()

