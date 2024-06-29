from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def say_hello(request):
    return HttpResponse("Hello World!")

def homepage(request):
    return HttpResponse("Welcome to the LittleLemon!")

def display_date(request):
    date_joined = datetime.today().date()
    return HttpResponse("The current date is: " + str(date_joined))

def menu(request):
    text = """<h1 style="color: #F4CE14;">Welcome to the LittleLemon Again from Menu!</h1>"""
    return HttpResponse(text)