from django.db import models


class Student(models.Model):
	stu_id = models.CharField(primary_key=True, max_length=20)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	b_date = models.CharField(max_length=20)
	telephone = models.CharField(max_length=14)
	gender = models.CharField(max_length=10)
	district = models.CharField(max_length=20)
	nationality = models.CharField(max_length=30)
	
