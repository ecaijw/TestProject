# Django ——从request中获取前端数据
# https://blog.csdn.net/qq_37049781/article/details/79705890
# django-admin.py startapp TestModel
# manage.py runserver 127.0.0.1:8000

mysql命令
https://www.cnblogs.com/dingjiaoyang/p/7026718.html
mysql>use dbname； 打开数据库：
mysql>show databases; 显示所有数据库
mysql>show tables; 显示数据库mysql中所有的表：先use mysql；然后
mysql>describe user; 显示表mysql数据库中user表的列信息）；


$ python3 manage.py migrate   # 创建表结构
$ python3 manage.py makemigrations TestModel  # 让 Django 知道我们在我们的模型有一些变更
$ python3 manage.py migrate TestModel   # 创建表结构

PS D:\other_cjwlaptop\install\python\django\TestProject> python .\manage.py makemigrations TestModel
Migrations for 'TestModel':
  TestModel\migrations\0001_initial.py
    - Create model Test
PS D:\other_cjwlaptop\install\python\django\TestProject> python .\manage.py migrate TestModel
Operations to perform:
  Apply all migrations: TestModel
Running migrations:
  Applying TestModel.0001_initial... OK
