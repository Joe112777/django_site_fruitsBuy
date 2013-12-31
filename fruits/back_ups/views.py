# Create your views here.
from django.http import HttpResponse
from django.forms.models import modelform_factory
from django.shortcuts import render
from fruits.models import Fruits
from fruits.models import Order

def search_form(request):
    return render(request, 'search_form.html')

def ordering(request):
    return render(request, 'fruitOrdering.html')

def orderNow(request):
    OrderForm = modelform_factory(Order)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        form.save()
    return render(request, 'fruitOrdering.html', {'form': OrderForm()})

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        fruit = Fruits.objects.filter(title__icontains=q)
        return render(request, 'search_results.html',{'fruits':fruit, 'query':q})
    else:
        return HttpResponse('Please submit a search term.') 
