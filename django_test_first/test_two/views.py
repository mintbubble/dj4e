from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse('Home Page')


def items(request):
    return HttpResponse('Items Page')


def items_num(request, a):
    return HttpResponse('Items Num Page %s' % a)

def items_day(request, year, month, day):
    return HttpResponse('Items Num Page %s.%s.%s' % (year,month,day ))

def book(request):
    return HttpResponse('')

def book_page(request, page=0):
    if page==0:
        return HttpResponse('Book')
    else:
        return HttpResponse('Book page %s' %page)
