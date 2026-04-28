from django.db import models
from django import forms
from .models import ContactUs, Sales


class ContactUsForm(forms.ModelForm):
	class Meta:
		model = ContactUs
		fields = ('name', 'phone', 'email', 'subject', 'message', )

	def __init__(self, *args, **kwargs):
		super(ContactUsForm, self).__init__(*args, **kwargs)
		self.fields["name"].widget.attrs['class'] = 'form-control form-input-field'
		self.fields["name"].widget.attrs['placeholder'] = 'Name'
		self.fields["name"].label = ''

		self.fields["phone"].widget.attrs['class'] = 'form-control form-input-field'
		self.fields["phone"].widget.attrs['placeholder'] = 'Phone'
		self.fields["phone"].label = ''

		self.fields["email"].widget.attrs['class'] = 'form-control form-input-field'
		self.fields["email"].widget.attrs['placeholder'] = 'Email'
		self.fields["email"].label = ''


		self.fields["subject"].widget.attrs['class'] = 'custom-dropdown w-100 h-100'
		self.fields["subject"].label = ''

		self.fields["message"].widget = forms.Textarea({
			'class': 'form-control form-input-field form-group-textarea',
			'rows': 6,
			'placeholder': 'Enter your message here...'
		})
		self.fields["message"].label = ''



class SalesForm(forms.Form):
	class Meta:
		model = Sales
		fields = '__all__'