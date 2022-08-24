from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def setcookie(request):
    response=HttpResponse("cookie set")
    response.set_cookie('python','networkzsystems.com')
    return response
def getcookie(request):
    language=request.COOKIES('python language')
    return HttpResponse("top programming langauge:"+language);