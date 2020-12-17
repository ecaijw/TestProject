from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from TestModel.models import Test
import time

def testdbAdd(request):
    data = 'runoob-' + time.strftime("%H:%M:%S", time.localtime())
    test1 = Test(name = data[0:20])
    test1.save()
    return HttpResponse("<p>Suceeded: added the data: {0}</p>".format(data))

def testdbUpdate(request):
    data = 'runoob-' + time.strftime("%H:%M:%S", time.localtime())
    # test1 = Test.objects.get(id = 1)
    list = Test.objects.order_by("id")
    if len(list) == 0:
        return HttpResponse("<p>empty set. Nothing to update")
    test1 = list[0]
    test1.name = data
    test1.save()
    # 另外一种方式
    # Test.objects.filter(id=1).update(name='Google')

    # 修改所有的列
    # Test.objects.all().update(name='Google')
    return HttpResponse("<p>Suceeded: updated the data: {0}</p>".format(data))

def testdbDelete(request):
    # test1 = Test.objects.get(id = 1)
    # get the first obj and delete
    list = Test.objects.order_by("id")
    if len(list) == 0:
        return HttpResponse("<p>empty set. Nothing to delete")
    test1 = list[0]
    data = test1.name
    test1.delete()
    # 另外一种方式
    # Test.objects.filter(id=1).delete()

    # 删除所有数据
    # Test.objects.all().delete()

    return HttpResponse("<p>Suceeded: deleted:" + data)

def testdbShow(request):
    # init
    response = ""
    response1 = ""

    # use objects to get all rows: select * from
    list = Test.objects.all()

    # filter = WHERE
    response2 = Test.objects.filter(id = 1)
    print(response2)

    # get one object
    try:
        response3 = Test.objects.get(id = 1)
        print(response3)
    except ObjectDoesNotExist:
        print("Failed to get the object")

    # limit returned data: OFFSET 0 LIMIT 2;
    Test.objects.order_by('name')[0:2]

    # sort
    Test.objects.order_by("id")

    Test.objects.filter(name = "runoob").order_by("id")
    print(Test.objects.all())

    if (len(list) == 0):
        return HttpResponse("<p>" + "empty set" + "<p>")
    else:
        # output all data
        for var in list:
            response1 += var.name + "<p>"
        response = response1
        return HttpResponse("<p>" + response + "<p>")