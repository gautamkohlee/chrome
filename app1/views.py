from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def viratkohli(request):
    return HttpResponse('<h1><marquee>king of coverdrive<h1/><marquee/>')
