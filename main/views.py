from django.shortcuts import render, redirect
from main.models import *
from . import views
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
def index(request):
	setting = Setting.objects.get(pk=1)
	header = Header.objects.all().order_by('-pub_date')
	product = Product.objects.all()
	service = Service.objects.all()
	testimonial = Testimonial.objects.all()
	context = {
			'setting':setting,
			'product':product,
			'testimonial': testimonial,
			'service': service,
			'header':header,
            }
	return render(request, "main/index.html", context )


def about(request):
	setting = Setting.objects.get(pk=1)
	product = Product.objects.all()
	service = Service.objects.all()
	testimonial = Testimonial.objects.all()
	context = {
			'setting':setting,
			'product':product,
			'testimonial': testimonial,
			'service':service,
            }
	return render(request, "main/about.html", context )

def services(request):
	pass


def product_detail(request, id, slug):
	setting = Setting.objects.get(pk=1)
	product = Product.objects.all()
	products = Product.objects.get(pk=id)
	service = Service.objects.all()
	images = Images.objects.filter(products_id=id)
	how_it_work = HowItWork.objects.filter(products_id=id)
	added_bonus = AddedBonus.objects.filter(products_id=id)
	top_feature = TopFeature.objects.filter(products_id=id)
		
	context = {
			'products':products,
			'product':product,
			'images':images,
			'how_it_work':how_it_work,
			'added_bonus':added_bonus,
			'top_feature':top_feature,
			'setting':setting,
			'service':service,
			}

	return render(request, 'main/product_detail.html', context)

def service_detail(request, id, slug):
	setting = Setting.objects.get(pk=1)
	product = Product.objects.all()
	service = Service.objects.all()
	services = Service.objects.get(pk=id)
	service_body = ServiceBody.objects.filter(service_id=id)
	service_process = ServiceProcess.objects.filter(service_id=id)
	service_header = ServiceHeader.objects.filter(service_id=id)
	service_feature = ServiceFeature.objects.filter(service_id=id)
		
	context = {
			'service': service,
			'service_header':service_header,
			'setting':setting,
			'services':services,
			'service_body':service_body,
			'service_process':service_process,
			'service_feature':service_feature,
			'product':product,
			}

	return render(request, 'main/service_detail.html', context)

def message(request):
	contacts = Contact.objects.all()

	context = {'contacts':contacts}
	return render(request, "contact/all_contacts.html", context)

def login_form(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "welcome "+user.username)
			current_user = request.user
			return HttpResponseRedirect('/setting')
		else:
			messages.warning(request, "Login Error !! username or password is incorrect")
			return HttpResponseRedirect('/login')
	setting = Setting.objects.all()
	current_user = request.user
	context = {
		'setting':setting,
	}
	return render(request, 'main/login_form.html', context)

@login_required(login_url='/login')
def setting(request):
	all_setting = Setting.objects.all()

	context = {'all_setting':all_setting}

	return render(request, 'main/setting.html', context)


def add_setting(request):
	form = SettingCreateForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, 'Successful')
		return redirect('/setting')
	context = {
		"form":form,
	}
	return render(request, "main/add_setting.html", context)



def update_setting(request, pk):
	queryset = Setting.objects.get(id=pk)
	form = SettingUpdateForm(instance=queryset)
	if request.method == 'POST':
		form = SettingUpdateForm(request.POST, request.FILES, instance=queryset)
		if form.is_valid():
			form.save()
			messages.success(request, 'updated')
			return redirect('/setting')

	context = {
		'form':form
	}

	return render(request, "main/add_setting.html", context)

def add_service(request):
	form = AddServiceForm(request.POST, request.FILES)
	if form.is_valid():
		form.save()
		messages.success(request, 'Successfully Added')
		return redirect('/')
	context = {
		"form":form
	}
	return render(request, "main/add_service.html", context)

def service_header(request):
	form = ServiceHeaderForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, 'Successfully added')
		return redirect('/')
	context = {
		'form':form,
	}
	return render(request, "main/service_header.html", context)


def service_process(request):
	form = ServiceProcessForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, 'Successfully added')
		return redirect('/')
	context = {
		'form':form,
	}
	return render(request, "main/service_header.html", context)

def service_feature(request):
	form = ServiceFeatureForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, 'Successfully Added')
		return redirect('/')
	context = {
			'form':form,
	}
	return render(request, 'main/service_header.html', context)


def service_body(request):
	form = ServiceBodyForm(request.POST, request.FILES)
	if form.is_valid():
		form.save()
		messages.success(request, 'Successfully Added')
		return redirect('/')
	context = {
		"form":form
	}
	return render(request, "main/service_header.html", context)

def all_service_header(request):
	service_header = ServiceHeader.objects.all()

	context = {'service_header': service_header}

	return render(request, 'main/all_service_header.html', context) 

def update_service_header(request, pk):
	queryset = ServiceHeader.objects.get(id=pk)
	form = ServiceHeaderUpdate(instance=queryset)
	if request.method == 'POST':
		form = SettingUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			messages.success(request, 'updated')
			return redirect('/setting')

	context = {
		'form':form
	}

	return render(request, "main/service_header_update.html", context)

