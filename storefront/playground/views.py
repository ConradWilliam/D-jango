from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Handles http requests
def say_hello(request):
    # return HttpResponse('Hello World')
    return render(request, 'hello.html', {'name': 'Conrad'})