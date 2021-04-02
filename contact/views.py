from django.shortcuts import render, redirect
from django.contrib import messages
from . import views
from .models import Contact, ContactForm
from main.models import Setting
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			data = Contact()
			data.name = form.cleaned_data['name']
			data.email = form.cleaned_data['email']
			data.phone = form.cleaned_data['phone']
			data.subject = form.cleaned_data['subject']
			data.message = form.cleaned_data['message']
			data.ip = request.META.get('REMOTE_ADDR')
			data.save()
			messages.success(request, "Your message has been delivered")
			return HttpResponseRedirect(reverse("contact"))

	form = ContactForm
	setting = Setting.objects.get(pk=1)
	
	context = {'form':form, 'setting':setting}
	return render(request,  "contact/contact.html", context)

