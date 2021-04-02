from django.db import models
from django.utils import timezone

# Create your models here.

class Setting(models.Model):

	title = models.CharField(max_length=150)
	keywords = models.CharField(max_length=350, null=True)
	description = models.CharField(max_length=350, null=True)
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

	def __str__(self):
		return self.title

class Product(models.Model):
	header = models.CharField(max_length=150)
	image = models.ImageField(upload_to='uploads/', blank=True, null=True)
	description = models.TextField()

	def __str__(self):
		return self.header

class WorkingProcess(models.Model):
	title = models.CharField(max_length=50, blank=True, null=True)
	details = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.title


class Testimonial(models.Model):
	name = models.CharField(max_length=150)
	position = models.CharField(max_length=50)
	testimony = models.TextField()

	def __str__(self):
		return self.name