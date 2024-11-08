from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
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
        # result = "No page for that topic!"
        # return HttpResponseNotFound(result)
        raise Http404("404 GECERIC ERROR")


# 사용자가 잘못된 topic 입력 시 redirection
def num_page_view(request, num_page):
    topics_list = list(articles.keys())
    topic = topics_list[num_page]

    return HttpResponseRedirect(topic)
