from django.db import models
from django.utils import timezone

# Create your models here.

class Setting(models.Model):

	title = models.CharField(max_length=150)
	keywords = models.TextField(blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	address = models.CharField(blank=True, max_length=150)
	company = models.CharField(blank=True, max_length=150)
	phone = models.CharField(blank=True, max_length=15)
	fax = models.CharField(blank=True, max_length=20)
	email = models.CharField(blank=True, max_length=50)
	smtpserver = models.CharField(blank=True, max_length=50)
	smtpemail = models.CharField(blank=True, max_length=50)
	smtppassword = models.CharField(blank=True, max_length=50)
	smtpport = models.CharField(blank=True, max_length=50)
	image = models.ImageField(upload_to='uploads/', blank=True, null=True)
	facebook = models.CharField(blank=True, max_length=50)
	instagram = models.CharField(blank=True, max_length=50)
	twitter = models.CharField(blank=True, max_length=50)
	aboutus = models.TextField(blank=True)
	contact = models.TextField(blank=True)
	footer_text = models.TextField(blank=True, null=True)
	references = models.TextField(blank=True)

	def __str__(self):
		return self.title

class Header(models.Model):
	title = models.CharField(max_length=150)
	image = models.ImageField(upload_to='uploads/', blank=True, null=True)
	content = models.TextField()
	pub_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

	def __str__(self):
		return self.title

class Product(models.Model):
	home_header = models.CharField(max_length=150, null=True, blank=True)
	home_icon = models.ImageField(upload_to='uploads/', blank=True, null=True)
	home_body = models.TextField(blank=True, null=True)
	header = models.CharField(max_length=150, blank=True, null=True)
	sbg_header_one = models.CharField(max_length=1000, null=True, blank=True)
	sbg_header_two = models.TextField(null=True, blank=True)
	image = models.ImageField(upload_to='uploads/', blank=True, null=True)
	description = models.TextField(blank=True)
	slug = models.SlugField(null=True, blank=True)

	def __str__(self):
		return self.home_header

class Testimonial(models.Model):
	name = models.CharField(max_length=150)
	position = models.CharField(max_length=50)
	testimony = models.TextField()

	def __str__(self):
		return self.name

class Images(models.Model):
	products = models.ForeignKey(Product, on_delete=models.CASCADE)
	title = models.CharField(max_length=50, blank=True)
	image = models.ImageField(upload_to='uploads/', blank=True, null=True)

	def __str__(self):
		return self.title

class HowItWork(models.Model):
	products = models.ForeignKey(Product, on_delete=models.CASCADE)
	icon = models.CharField(max_length=120, blank=True)
	title = models.CharField(max_length=200, blank=True)
	detail = models.TextField()

	def __str__(self):
		return self.title

class AddedBonus(models.Model):
	products = models.ForeignKey(Product, on_delete=models.CASCADE)
	icon = models.CharField(max_length=120, blank=True)
	title = models.CharField(max_length=200, blank=True)
	detail = models.TextField()

	def __str__(self):
		return self.title

class TopFeature(models.Model):
	products = models.ForeignKey(Product, on_delete=models.CASCADE)
	detail_one = models.TextField()

class Service(models.Model):
	title = models.CharField(max_length=200, blank=True, null=True)
	image = models.ImageField(upload_to='uploads/', blank=True, null=True) 
	slug = models.SlugField(null=True, blank=True, default="slug")

	def __str__(self):
		return self.title

class ServiceHeader(models.Model):
	service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)
	shc_one = models.CharField(max_length=200, blank=True, null=True)
	shc_two = models.TextField(blank=True, null=True)

class ServiceBody(models.Model):
	service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)
	sbhcontent_one = models.CharField(max_length=200, blank=True, null=True)
	sbhcontent_two = models.TextField(blank=True, null=True)
	sbhimage = models.ImageField(upload_to='uploads/', blank=True, null=True)
	sbdetails = models.TextField(blank=True, null=True)

class ServiceProcess(models.Model):
	service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)
	process_icon = models.CharField(max_length=200, blank=True, null=True)
	process_title = models.CharField(max_length=200, blank=True, null=True)

class ServiceFeature(models.Model):
	service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)
	process_icon = models.CharField(max_length=200, blank=True, null=True)
	process_title = models.CharField(max_length=200, blank=True, null=True)
	description = models.TextField(blank=True, null=True)











	