from django.db import models


class Staff(models.Model):
	staff_id = models.CharField(primary_key=True, max_length=10)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	b_date = models.CharField(max_length=9)
	telephone = models.CharField(max_length=14)
	gender = models.CharField(max_length=6)
	district = models.CharField(max_length=20)
	nationality = models.CharField(max_length=30)
	
	