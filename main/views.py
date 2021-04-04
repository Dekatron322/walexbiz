from django.shortcuts import render
from main.models import *
from . import views
# Create your views here.
def index(request):
	setting = Setting.objects.get(pk=1)
	product = Product.objects.all()
	service = Service.objects.all()
	testimonial = Testimonial.objects.all()
	context = {
			'setting':setting,
			'product':product,
			'testimonial': testimonial,
			'service': service,
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


def product_detail(request, id):
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

def service_detail(request, id):
	setting = Setting.objects.get(pk=1)
	product = Product.objects.all()
	service = Service.objects.all()
	services = Service.objects.get(pk=id)
	service_body = ServiceBody.objects.filter(service_id=id)
	service_process = ServiceProcess.objects.filter(service_id=id)
	service_header = ServiceHeader.objects.filter(service_id=id)
		
	context = {
			'service': service,
			'service_header':service_header,
			'setting':setting,
			'services':services,
			'service_body':service_body,
			'service_process':service_process,
			'product':product,
			}

	return render(request, 'main/service_detail.html', context)