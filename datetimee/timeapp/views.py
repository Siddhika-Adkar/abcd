from django.shortcuts import render
import datetime
from django.http import HttpResponse
# Create your views here.
def display(req):
    date=datetime.datetime.now()
    s='<h2> the current Date and Time is time is:'+str(date)+'</h2>'
    return HttpResponse(s)
