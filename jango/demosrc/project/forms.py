from django import forms 

from .models import ContactUs


class Contact_Form(forms.ModelForm):
	class Meta:
		model = ContactUs
		fields = [
			'name',
			'email',
			'phone',
			'complain'
		]
