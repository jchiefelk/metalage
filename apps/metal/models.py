from django.db import models


class Metal(models.Model):
    museum_number=models.CharField(max_length=255)
    country=models.CharField(max_length=50)
    site=models.CharField(max_length=255)
    description=models.CharField(max_length=50)
    analysis_method=models.CharField(max_length=50)
    source=models.CharField(max_length=255)
