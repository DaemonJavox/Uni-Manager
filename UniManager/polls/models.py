from django.db import models

class Credentials(models.Model):
	user_name = models.CharField(max_length=100)
	user_email = models.CharField(max_length=200)
	user_password = models.CharField(max_length=200)
	
class DataImage(models.Model):
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=1000)
	link_news = models.CharField(max_length=200)
	credit = models.CharField(max_length=100)
	category = models.CharField(max_length=100)
	image = models.CharField(max_length=500)
