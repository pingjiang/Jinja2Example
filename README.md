# Jinja2 入门示例

今天移植gist-it的时候发现了这个库，顺便的了解和学习了一下。这里简单的记录一下。

## 学习目标

* 布局模板的实现。
* 页面模板的实现。
* 视图变量。
* 逻辑判断。
* 循环控制。
* 标签，控件或宏定义。

## 快速入门

### 使用block/endblock定义块占位符
```
	
	<!doctype html>
	<html lang="en">
	<head>
	    <meta charset="UTF-8" />
	    {% block head %}
	    <title>{% block title %}{% endblock %} - Jinja2 入门示例</title>
	    {% endblock %}
	</head>
	<body>
	    <div id="content">
	        {% block content %}{% endblock %}
	    </div>
	    
	    <div id="footer">
	        {% block footer %}
	        &copy; Copyright 2014 by <a href="http://domain.invalid/">PUB2ME</a>.
	        {% endblock %}
	    </div>
	</body>
	</html>

```

### 基于视图模板定义页面
```
	
	{% extends 'layout.html' %}
	{% block title %}成员列表{% endblock %}
	{% block content %}
	  <ul>
	  {% for user in users %}
	    <li><a href="{{ user.url }}">{{ user.username }}</a></li>
	  {% endfor %}
	  </ul>
	{% endblock %}
	
```

### 示例代码
加载模板，注入数据，渲染模板。
```
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

```

### 结果页面
```
	
	<!doctype html>
	<html lang="en">
	<head>
	    <meta charset="UTF-8" />
	    
	    <title>成员列表 - Jinja2 入门示例</title>
	    
	</head>
	<body>
	    <div id="content">
	        
	  <ul>
	  
	    <li><a href="http://blog.pub2me.com">PUB2ME</a></li>
	  
	  </ul>
	
	    </div>
	    
	    <div id="footer">
	        
	        &copy; Copyright 2014 by <a href="http://domain.invalid/">PUB2ME</a>.
	        
	    </div>
	</body>
	</html>
	
```

## 参考文档

* [http://jinja.pocoo.org/docs](http://jinja.pocoo.org/docs)
* [项目GitHub首页](https://github.com/mitsuhiko/jinja2)
