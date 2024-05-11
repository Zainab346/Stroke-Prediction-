from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    marital_status = models.CharField(max_length=50)
    work_type = models.CharField(max_length=50)
    residence = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    bmi = models.FloatField()
    gluc_level = models.FloatField()
    smoke = models.CharField(max_length=50)
    hypertension = models.CharField(max_length=50)
    heart_disease = models.CharField(max_length=50)


