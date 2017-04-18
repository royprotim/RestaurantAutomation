from django.db import models

# Create your models here.


class Employee(models.Model):
	emp_id = models.CharField(max_length=10)
	emp_type = models.CharField(max_length=20)
	emp_firstname = models.CharField(max_length=50)
	emp_lastname = models.CharField(max_length=50)
	emp_hours = models.DecimalField(max_digits=4,decimal_places=2)
