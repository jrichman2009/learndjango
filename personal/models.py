from django.db import models

# Create your models here.
class Site_pixel(models.Model):
	

	site = models.CharField(max_length = 120)
	pixel = models.CharField(max_length = 48)
	date = models.CharField(max_length = 12)
	requestURL = models.CharField(max_length = 120)

	def __str__(self):
		return self.pixel
	
	
		
	
	
	


