from django.shortcuts import render
from django.http import HttpResponse
from product.models import Laptop
# Create your views here.
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
	return render(request, "laptop.html", context)


def about_view(request, *args, **kwargs):
	return render(request, "about.html", {})


def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})