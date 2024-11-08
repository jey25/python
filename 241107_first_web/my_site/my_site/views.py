
from django.http.response import HttpResponse

# Create your views here.

def home_view(request):
    return HttpResponse("home View")