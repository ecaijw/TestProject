from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def hello(request):
    return HttpResponse("你好，Hello world! ver 2.0")

# add an object
# 可以看到，我们这里使用render来替代之前使用的HttpResponse。render还使用了一个字典context作为参数。
# context字典中元素的键值hello对应了模板中的变量{{hello}}。
def runoob(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'runoob.html', context)

# 模板语法：
#
# view：｛"HTML变量名" : "views变量名"｝
# HTML：｛｛变量名｝｝
def runoob2(request):
    views_name = "菜鸟教程"
    return render(request, 'runoob2.html', {"name":views_name})

# 列表：可以用 . 索引下标取出对应的元素。
# 字典: 可以用 .键 取出对应的值。
def runoob3(request):
    context = {}
    context['views_list'] = ["菜鸟教程1", "菜鸟教程2", "菜鸟教程3"]
    context['views_dict'] = {"name" : "菜鸟教程 dict"}

    # # try filter: default
    # {{ default_text|default:"菜鸟教程666" }}
    # # try filter: length
    # <p>{{ views_dict | length }}</p>

    # # try filter: filesizeformat
    # <p>{{ num1 | default: 123456789 | filesizeformat }}</p>
    # <p>{{ num2 | filesizeformat }}</p>
    context['num2'] = 97531

    # # try filter: datetime
    # <p>{{ time |  datetime }}</p>
    import datetime
    context['time'] = datetime.datetime.now()

    context['num'] = 59
    context['views_str'] =  "<a href='https://www.runoob.com/'>点击跳转</a>"

    context['athlete_list'] = [
    {'name':'Apple','age':'22','hight':'171'},
    {'name':'Banana','age':'23','hight':'165'},
    {'name':'Cat','age':'24','hight':'148'},
    {'name':'Dog','age':'25','hight':'166'}]

    # return render(request, 'runoob3.html', {"views_list":views_list, "views_dict":views_dict})
    return render(request, 'runoob3.html', context)