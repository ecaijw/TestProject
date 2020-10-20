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