from .models import *
from contact.models import *
from django.forms import *
from django import forms

class SettingCreateForm(forms.ModelForm):
	class Meta:
		model = Setting
		fields = ['title', 'keywords','description', 'company', 'phone', 'fax', 'email','image','footer_logo','fav','facebook', 'instagram', 'aboutus', 'footer_text', 'references', 'contact', 'twitter']

class SettingUpdateForm(forms.ModelForm):
	class Meta:
		model = Setting
		fields = ['title', 'keywords','description', 'company', 'phone', 'fax', 'email','image','footer_logo','fav','facebook', 'instagram', 'aboutus', 'footer_text', 'references', 'contact', 'twitter']

class AddServiceForm(forms.ModelForm):
	title = forms.CharField(max_length=200)
	image = forms.ImageField() 
	class Meta:
		model = Service
		fields = ('title', 'image')


	def clean_title(self):
		title = self.cleaned_data.get('title')
		image = self.cleaned_data.get('image')
		
		for instance in Service.objects.all():
			if instance.title == title:

				raise forms.ValidationError(title + ' is already created')
		return title

class ServiceHeaderForm(forms.ModelForm):
	class Meta:
		model = ServiceHeader
		fields = ['service', 'shc_one', 'shc_two']

	def clean_service(self):
		service = self.cleaned_data.get('service')
		if not service:
			raise forms.ValidationError('this field is required')

		return service

class ServiceHeaderUpdate(forms.ModelForm):
	class Meta:
		model = ServiceHeader
		fields = ['service', 'shc_one', 'shc_two']


class ServiceBodyForm(forms.ModelForm):
	class Meta:
		model = ServiceBody
		fields = ['service', 'sbhcontent_one', 'sbhimage', 'sbhcontent_two', 'sbdetails']

	def clean_service(self):
		service = self.cleaned_data.get('service')
		if not service:
			raise forms.ValidationError('this field is required')

		return service

class ServiceProcessForm(forms.ModelForm):
	class Meta:
		model = ServiceProcess
		fields = ['service', 'process_icon', 'process_title']

	def clean_service(self):
		service = self.cleaned_data.get('service')
		if not service:
			raise forms.ValidationError('this field is required')

		return service

class ServiceFeatureForm(forms.ModelForm):
	class Meta:
		model = ServiceFeature
		fields = ['service', 'process_icon', 'process_title', 'description']

	def clean_service(self):
		service = self.cleaned_data.get('service')
		if not service:
			raise forms.ValidationError('this field is required')

		return service


