#coding:utf-8
import os

import tornado.web
import tornado.ioloop


import logging
from login import LoginHandler
from login import LogoutHandler
from project import ProjectHandler,DeployHandler
from admin import AdminHandler

from manager.manager_user import UserHandler, Edit_UserHandler, Del_UserHandler
from manager.manager_grp import GroupHandler, Del_GroupHanler, Edit_GroupHanler
from manager.manager_host import HostHandler,Edit_HostHandler,Del_HostHandler

handlers=[
		(r'/',LoginHandler),
        (r'/project',ProjectHandler),
        (r'/deploy',DeployHandler),
		(r'/logout',LogoutHandler),
		(r"/op-admin",AdminHandler),
		(r"/manager_user",UserHandler),
		(r"/edit_user",Edit_UserHandler),
		(r"/del_user",Del_UserHandler),
		(r"/manager_group",GroupHandler),
		(r"/del_grp",Del_GroupHanler),
		(r"/edit_grp",Edit_GroupHanler),
        (r"/del_host",Del_HostHandler),
		(r"/manager_host",HostHandler),
        (r"/edit_host",Edit_HostHandler)
		]
settings={
		'debug' : False,
		'static_path':os.path.join(os.path.dirname(__file__),'static'),
		'template_path':os.path.join(os.path.dirname(__file__),'template'),
		'cookie_secret': 'bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=',
		'login_url':'/',
		}

app=tornado.web.Application(handlers,**settings)
# options.parse_command_line()
logging.debug("debug ...")
# options.parse_command_line()
app.listen(88)
tornado.ioloop.IOLoop.instance().start()
