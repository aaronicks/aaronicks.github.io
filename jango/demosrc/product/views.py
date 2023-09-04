from django.shortcuts import render
from django.http import HttpResponse
from product.models import Laptop
from .forms import LaptopForm

# Create your views here.

def laptops_view(request, *args, **kwargs):
	form = LaptopForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = LaptopForm()

	context = {

		'form':form
	}

	return render(request, "mkts/laptop_creat.html", context)





def laptop_view(request, *args, **kwargs):
	objt = Laptop.objects.get(id=1)
	#context = {
		#"memory":obj.ram,
		#"graphics": obj.graphics,
		#"os":obj.os,
		#"battery":obj.battery
	#}
	context = {
		"obj": objt
	}
	return render(request, "mkts/laptop_detail.html", context)


def about_view(request, *args, **kwargs):
	return render(request, "about.html", {})


def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})