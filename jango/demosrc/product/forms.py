from django import forms

from .models import Laptop


class LaptopForm(forms.ModelForm):
	class Meta:
		model = Laptop
		fields = [
			'storage',
			"ram",
			'graphics',
			'wireless',
			'os',
			'usb_port',
			'battery',
			'screen_size',
			'price'
		] 

