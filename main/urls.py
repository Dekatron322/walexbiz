from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('about/', views.about, name='about'),
	path('services/', views.services, name='services'),
	path('product/<int:id>', views.product_detail, name='product_detail'),
]