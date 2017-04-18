from django.shortcuts import render
from django.http import HttpResponse
from . models import FoodItem
from orders.models import Orders
from django.forms.formsets import formset_factory
from django.contrib import messages
from django.core.urlresolvers import reverse

# Create your views here.
def menu(request):
	if request.method == 'POST':
            order_req=request.POST.getlist('order[]')
            for id in order_req:
            	Orders.objects.create_order(id,2,'N')
            return HttpResponse("Order done!");
	else:
		all_entries = FoodItem.objects.all()		
		return render(request, "menu.html",{'menu':all_entries})