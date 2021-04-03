from django.contrib import admin
from main.models import *
# Register your models here.
class ProductsImageInline(admin.TabularInline):
    model = Images
    readonly_fields = ('id',)
    extra = 1

class HowItWorkInline(admin.TabularInline):
    model = HowItWork
    readonly_fields = ('id',)
    extra = 1

class AddedBonusInline(admin.TabularInline):
    model = AddedBonus
    readonly_fields = ('id',)
    extra = 1

class TopFeatureInline(admin.TabularInline):
    model = TopFeature
    readonly_fields = ('id',)
    extra = 1

class ServiceHeaderInline(admin.TabularInline):
    model = ServiceHeader
    readonly_fields = ('id',)
    extra = 1

class ServiceBodyInline(admin.TabularInline):
    model = ServiceBody
    readonly_fields = ('id',)
    extra = 1

class ServiceProcessInline(admin.TabularInline):
    model = ServiceProcess
    readonly_fields = ('id',)
    extra = 1

class ServiceAdmin(admin.ModelAdmin):
	inlines = [ServiceHeaderInline, ServiceBodyInline, ServiceProcessInline]

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductsImageInline, HowItWorkInline, AddedBonusInline, TopFeatureInline]


admin.site.register(Setting)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Testimonial)