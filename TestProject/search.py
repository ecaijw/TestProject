from django.http import HttpResponse
from django.shortcuts import render

# handle form
def search_form(request):
    return render(request, "search_form.html")

def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET and request.GET['q']:
        message = 'your search: ' +  request.GET['q']
    else:
        message = 'your search: empty form'
    return HttpResponse(message)
