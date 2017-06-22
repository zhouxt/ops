from db import db_operation

from admin import AdminHandler
import dh


a=db_operation().select('select * from user')
for i in a:
    print i