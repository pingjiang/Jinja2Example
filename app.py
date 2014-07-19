#!/usr/bin/env python
#--*-- coding: UTF-8 --*--

from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('.'))

class User(object):
    """docstring for User"""
    def __init__(self, username, url):
        super(User, self).__init__()
        self.username = username
        self.url = url
        
template = env.get_template('users.html')
print template.render(users = [User('PUB2ME', 'http://blog.pub2me.com')])
