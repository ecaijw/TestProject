from django.http import HttpResponse
from TestModel.models import Test

def testdb(request):
    test1 = Test(name = 'runoob')
    test1.save()
    return HttpResponse("<p>Suceeded: add the data</p>")
