from django.shortcuts import render
from main.models import Setting, Product, Testimonial
from . import views
# Create your views here.
def index(request):
	setting = Setting.objects.get(pk=1)
	product = Product.objects.all()
	testimonial = Testimonial.objects.all()
	context = {
			'setting':setting,
			'product':product,
			'testimonial': testimonial,
            }
	return render(request, "main/index.html", context )


def about(request):
	setting = Setting.objects.get(pk=1)
	product = Product.objects.all()
	testimonial = Testimonial.objects.all()
	context = {
			'setting':setting,
			'product':product,
			'testimonial': testimonial,
            }
	return render(request, "main/about.html", context )

def services(request):
	pass


def product_detail(request, id):
	product = Product.objects.get(pk=id)
		
	context = {
			'product':product
			}

	return render(request, 'main/product_detail.html', context)