from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def index(requst):
	return HttpResponse("hi hi hi hi")