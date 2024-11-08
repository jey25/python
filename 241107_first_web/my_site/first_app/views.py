from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.


articles = {
    'contents':'History page',
    'test':'etc page'
}

def new_view(request, topic):
    return HttpResponse(articles[topic])

