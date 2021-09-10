from django.db import models

# Create your models here.

class doctor1(models.Model):
    name=models.CharField(max_length=50)
    special=models.CharField(max_length=50)
    hospital = models.CharField(max_length=50)
    salary = models.CharField(max_length=50)
    photo = models.CharField(max_length=50)
    class Meta:
        db_table='doctor1'

class patient1(models.Model):
    name=models.CharField(max_length=50)
    doctor=models.CharField(max_length=50)
    bill = models.CharField(max_length=50)
    hospital = models.CharField(max_length=50)
    photo = models.CharField(max_length=50)
    class Meta:
        db_table='patient1'


class sp1(models.Model):
    category_id=models.CharField(max_length=50)
    special=models.CharField(max_length=50)
    class Meta:
        db_table='specialization1'