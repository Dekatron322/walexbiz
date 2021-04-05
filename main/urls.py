from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('about/', views.about, name='about'),
	path('services/', views.services, name='services'),
	path('product/<int:id>/<slug:slug>', views.product_detail, name='product_detail'),
	path('service/<int:id>/<slug:slug>', views.service_detail, name='service_detail'),
]