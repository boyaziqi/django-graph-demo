python django graph demo
-----
基于 Django 写的一个 graph 应用，实现基本的文章及分类管理。

#### 使用
- 更改 settings 里的数据库配置，本 demo 默认使用 MySQL，如果要使用其他数据库，需要安装对于的包

- 运行 `python manage.py migrate` 迁移数据库

- 运行 `python manage.py runserver` 启动测试服务器

- 访问 http://127.0.0.1:8000/graphq，将会打开一个 GraphIQL 窗口，可以在里面进行测试。

#### 运行效果
![image](http://)