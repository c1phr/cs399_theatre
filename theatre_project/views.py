from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request, 'index.html', {})

def information_performance(request):
	return render(request, 'information_performance.html', {})

def merchandise(request):
	return render(request, 'merchandise.html', {})

def performances(request):
	return render(request, 'performances.html', {})
    
    
def ticket_sales(request):
	return render(request, 'ticket_sales.html', {})

