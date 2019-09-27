from django.db import models


class ElementTraceAssay(models.Model):
    analysis_method = models.CharField(max_length=50,blank=True, null=True)
    iron_ppm = models.IntegerField(blank=True, null=True)
    arsenic_ppm = models.IntegerField(blank=True, null=True)
    cobalt_ppm = models.IntegerField(blank=True, null=True)
    copper_ppm = models.IntegerField(blank=True, null=True)
    silver_ppm = models.IntegerField(blank=True, null=True)
    gold_ppm = models.IntegerField(blank=True, null=True)
    chromium_ppm = models.IntegerField(blank=True, null=True)
    zinc_ppm = models.IntegerField(blank=True, null=True)
    cobalt_ppm = models.IntegerField(blank=True, null=True)
    nickel_ppm = models.IntegerField(blank=True, null=True)
    antimony_ppm = models.IntegerField(blank=True, null=True)
    sulfur_ppm = models.IntegerField(blank=True, null=True)
    bismuth = models.IntegerField(blank=True, null=True)
    cadmium = models.IntegerField(blank=True, null=True)
    indium = models.IntegerField(blank=True, null=True)
    manganese = models.IntegerField(blank=True, null=True)
    lead = models.IntegerField(blank=True, null=True)
    selenium = models.IntegerField(blank=True, null=True)
    tellurium = models.IntegerField(blank=True, null=True)    

class Metal(models.Model):
    museum_number=models.CharField(max_length=255)
    country=models.CharField(max_length=50)
    site=models.CharField(max_length=255)
    description=models.CharField(max_length=50)
    source=models.CharField(max_length=255)
    element_trace_assay_id = models.ForeignKey(ElementTraceAssay, on_delete=models.PROTECT, blank=True, null=True)
