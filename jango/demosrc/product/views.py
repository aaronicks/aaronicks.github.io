from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def laptop_view(request, *args, **kwargs):
	print(args, kwargs)
	return render(request, "laptop.html", {})


def about_view(request, *args, **kwargs):
	return render(request, "about.html", {})


def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})