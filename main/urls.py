from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('about/', views.about, name='about'),
	path('service_body/', views.service_body, name='service_body'),
	path('service_header/', views.service_header, name='service_header'),
	path('service_process/', views.service_process, name='service_process'),
	path('service_feature/', views.service_feature, name='service_feature'),
	path('add_service/', views.add_service, name='add_service'),
	path('add_setting/', views.add_setting, name='add_setting'),
	path('login/', views.login_form, name='login_form'),
	path('services/', views.services, name='services'),
	path('setting/', views.setting, name='setting'),
	path('all_service_header/', views.all_service_header, name='all_service_header'),
	path('message/', views.message, name='message'),
	path('product/<int:id>/<slug:slug>', views.product_detail, name='product_detail'),
	path('service/<int:id>/<slug:slug>', views.service_detail, name='service_detail'),
	path('update_setting/<str:pk>/', views.update_setting, name='update_setting'),
	path('update_service_header/<str:pk>/', views.update_service_header, name='update_service_header'),
]