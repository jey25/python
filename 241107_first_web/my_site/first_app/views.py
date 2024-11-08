from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound
# Create your views here.


articles = {
    'contents':'History page',
    'test':'etc page'
}

def first_view(request):
    return HttpResponse("first page")

def new_view(request, topic):
    try:
        result = articles[topic]
        return HttpResponse(result)
    except:
        result = "No page for that topic!"
        return HttpResponseNotFound(result)



