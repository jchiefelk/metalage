from django.db import models


class ElementTraceAssay(models.Model):
    analysis_method = models.CharField(max_length=50, blank=True, null=True)
    iron_ppm = models.CharField(max_length=50, blank=True, null=True)
    arsenic_ppm = models.CharField(max_length=50, blank=True, null=True)
    cobalt_ppm = models.CharField(max_length=50, blank=True, null=True)
    copper_ppm = models.CharField(max_length=50, blank=True, null=True)
    silver_ppm = models.CharField(max_length=50, blank=True, null=True)
    gold_ppm = models.CharField(max_length=50, blank=True, null=True)
    chromium_ppm = models.CharField(max_length=50, blank=True, null=True)
    zinc_ppm = models.CharField(max_length=50, blank=True, null=True)
    cobalt_ppm = models.CharField(max_length=50, blank=True, null=True)
    nickel_ppm = models.CharField(max_length=50, blank=True, null=True)
    antimony_ppm = models.CharField(max_length=50, blank=True, null=True)
    sulfur_ppm = models.CharField(max_length=50, blank=True, null=True)
    bismuth_ppm = models.CharField(max_length=50, blank=True, null=True)
    cadmium_ppm = models.CharField(max_length=50, blank=True, null=True)
    indium_ppm = models.CharField(max_length=50, blank=True, null=True)
    manganese_ppm = models.CharField(max_length=50, blank=True, null=True)
    lead_ppm = models.CharField(max_length=50, blank=True, null=True)
    selenium_ppm = models.CharField(max_length=50, blank=True, null=True)
    tellurium_ppm = models.CharField(max_length=50, blank=True, null=True)    
    tin_ppm = models.CharField(max_length=50, blank=True, null=True)
    magnesium_ppm = models.CharField(max_length=50, blank=True, null=True)
    aluminum_ppm = models.CharField(max_length=50, blank=True, null=True)
    silicon_ppm = models.CharField(max_length=50, blank=True, null=True)
    phosphorous_ppm = models.CharField(max_length=50, blank=True, null=True)
    scandium_ppm = models.CharField(max_length=50, blank=True, null=True)
    titanium_ppm = models.CharField(max_length=50, blank=True, null=True)
    vanadium_ppm = models.CharField(max_length=50, blank=True, null=True)
    molybdenum_ppm = models.CharField(max_length=50, blank=True, null=True)
    rhodium_ppm = models.CharField(max_length=50, blank=True, null=True)
    cadmium_ppm = models.CharField(max_length=50, blank=True, null=True)
    indium_ppm = models.CharField(max_length=50, blank=True, null=True)
    tellurium_ppm = models.CharField(max_length=50, blank=True, null=True)
    lanthanum_ppm = models.CharField(max_length=50, blank=True, null=True)
    cerium_ppm = models.CharField(max_length=50, blank=True, null=True)
    tantalum_ppm = models.CharField(max_length=50, blank=True, null=True)
    tungsten_ppm = models.CharField(max_length=50, blank=True, null=True)
    platinum_ppm = models.CharField(max_length=50, blank=True, null=True)
    mercury_ppm = models.CharField(max_length=50, blank=True, null=True)
    uranium_ppm = models.CharField(max_length=50, blank=True, null=True)
    sodium_ppm = models.CharField(max_length=50, blank=True, null=True)
    sodium_percent = models.CharField(max_length=50, blank=True, null=True)
    uranium_percent = models.CharField(max_length=50, blank=True, null=True)
    mercury_percent = models.CharField(max_length=50, blank=True, null=True)
    platinum_percent = models.CharField(max_length=50, blank=True, null=True)    
    tungsten_percent = models.CharField(max_length=50, blank=True, null=True)
    tantalum_percent = models.CharField(max_length=50, blank=True, null=True)
    cerium_percent = models.CharField(max_length=50, blank=True, null=True)
    lanthanum_percent = models.CharField(max_length=50, blank=True, null=True)
    tellurium_percent = models.CharField(max_length=50, blank=True, null=True)    
    cadmium_percent = models.CharField(max_length=50, blank=True, null=True)    
    rhodium_percent = models.CharField(max_length=50, blank=True, null=True)
    molybdenum_percent = models.CharField(max_length=50, blank=True, null=True)
    vanadium_percent = models.CharField(max_length=50, blank=True, null=True)
    titanium_percent = models.CharField(max_length=50, blank=True, null=True)
    scandium_percent = models.CharField(max_length=50, blank=True, null=True)
    phosphorous_percent = models.CharField(max_length=50, blank=True, null=True)
    silicon_percent = models.CharField(max_length=50, blank=True, null=True)
    aluminum_percent = models.CharField(max_length=50, blank=True, null=True)
    magnesium_percent = models.CharField(max_length=50, blank=True, null=True)
    iron_percent = models.CharField(max_length=50, blank=True, null=True)
    arsenic_percent = models.CharField(max_length=50, blank=True, null=True)
    cobalt_percent = models.CharField(max_length=50, blank=True, null=True)
    copper_percent = models.CharField(max_length=50, blank=True, null=True)
    silver_percent = models.CharField(max_length=50, blank=True, null=True)
    gold_percent = models.CharField(max_length=50, blank=True, null=True)
    chromium_percent = models.CharField(max_length=50, blank=True, null=True)
    zinc_percent = models.CharField(max_length=50, blank=True, null=True)
    cobalt_percent = models.CharField(max_length=50, blank=True, null=True)
    nickel_percent = models.CharField(max_length=50, blank=True, null=True)
    antimony_percent = models.CharField(max_length=50, blank=True, null=True)
    sulfur_percent = models.CharField(max_length=50, blank=True, null=True)
    bismuth_percent = models.CharField(max_length=50, blank=True, null=True)
    cadmium_percent = models.CharField(max_length=50, blank=True, null=True)
    indium_percent = models.CharField(max_length=50, blank=True, null=True)
    manganese_percent = models.CharField(max_length=50, blank=True, null=True)
    lead_percent = models.CharField(max_length=50, blank=True, null=True)
    selenium_percent = models.CharField(max_length=50, blank=True, null=True)
    tellurium_percent = models.CharField(max_length=50, blank=True, null=True)    
    tin_percent = models.CharField(max_length=50, blank=True, null=True)


class IsotopeTraceAssay(models.Model):
    analysis_method = models.CharField(max_length=50, blank=True, null=True)
    delta_copper_65 = models.CharField(max_length=50, blank=True, null=True)
    lead_208_to_206 = models.CharField(max_length=50, blank=True, null=True)
    lead_207_to_206 = models.CharField(max_length=50, blank=True, null=True)
    lead_206_to_204 = models.CharField(max_length=50, blank=True, null=True)


class Metal(models.Model):
    museum_number = models.CharField(max_length=255)
    time_period = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    site = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    element_trace_assay_id = models.ForeignKey(ElementTraceAssay, on_delete=models.CASCADE, blank=True, null=True)
    isotope_trace_assay_id = models.ForeignKey(IsotopeTraceAssay, on_delete=models.CASCADE, blank=True, null=True)


class Ore(models.Model):
    museum_number = models.CharField(max_length=255)
    country = models.CharField(max_length=50)
    site = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    element_trace_assay_id = models.ForeignKey(ElementTraceAssay, on_delete=models.CASCADE, blank=True, null=True)
    isotope_trace_assay_id = models.ForeignKey(IsotopeTraceAssay, on_delete=models.CASCADE, blank=True, null=True)
