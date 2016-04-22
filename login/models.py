from django.db import models
from django.utils import timezone

class log_in(models.Model):
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=100)

	def __str__(self):
		return self.username