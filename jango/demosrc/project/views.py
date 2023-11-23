from django.shortcuts import render
from django.http import HttpResponse
from project.models import ContactUs
from .forms import Contact_Form

# Create your views here.

def contact_forms(request, *args, **kwargs):
	forms = Contact_Form(request.POST or None)
	if forms.is_valid():
		forms.save()
		forms = Contact_Form()
	context = {

		"frm":forms
	}
	return render(request, "conta/contact_forms.html", context)


def contact_views(request, *args, **kwargs):
	objt = ContactUs.objects.get(id=1)
	context = {
		"obj":objt

	}
	return render(request, "conta/contact.html", context)

