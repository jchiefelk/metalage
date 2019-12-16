from apps.metal.models import Metal
from apps.metal.models import Ore
from apps.metal.models import ElementTraceAssay
from apps.metal.models import IsotopeTraceAssay
import pdb


def run(*args):
    metal = Metal.objects.all().values()
    for _object in metal:
        if _object['country'] == 'USA':
            if _object['description'] == 'Geological Source Sample':
                if _object['element_trace_assay_id_id'] == None:
                    isotope_trace = IsotopeTraceAssay.objects.get(id=_object['isotope_trace_assay_id_id'])
                    _ore = Ore(
	                    museum_number = _object['museum_number'],
	                    country = _object['country'],
	                    site = _object['site'],
	                    description = _object['description'],
	                    mineral='Native Copper',
	                    source = _object['source'],
	                    isotope_trace_assay_id = isotope_trace
                    )
                    _ore.save()
                    Metal.objects.filter(id=_object['id']).delete()

                if _object['isotope_trace_assay_id_id'] == None:    
                    element_trace = ElementTraceAssay.objects.get(id=_object['element_trace_assay_id_id'])
                    _ore = Ore(
	                    museum_number = _object['museum_number'],
	                    country = _object['country'],
	                    site = _object['site'],
	                    description = _object['description'],
	                    mineral='Native Copper',
	                    source = _object['source'],
	                    element_trace_assay_id = element_trace
                    )
                    _ore.save()
                    Metal.objects.filter(id=_object['id']).delete()
            if _object['description'] == 'Ore':
                if _object['element_trace_assay_id_id'] == None:
                    isotope_trace = IsotopeTraceAssay.objects.get(id=_object['isotope_trace_assay_id_id'])
                    _ore = Ore(
	                    museum_number = _object['museum_number'],
	                    country = _object['country'],
	                    site = _object['site'],
	                    description = _object['description'],
	                    mineral='Native Copper',
	                    source = _object['source'],
	                    isotope_trace_assay_id = isotope_trace
                    ) 
                    _ore.save()
                    Metal.objects.filter(id=_object['id']).delete()
                if _object['isotope_trace_assay_id_id'] == None:    
                    element_trace = ElementTraceAssay.objects.get(id=_object['element_trace_assay_id_id'])
                    _ore = Ore(
	                    museum_number = _object['museum_number'],
	                    country = _object['country'],
	                    site = _object['site'],
	                    description = _object['description'],
	                    mineral='Native Copper',
	                    source = _object['source'],
	                    element_trace_assay_id = element_trace
                    )     
                    _ore.save()
                    Metal.objects.filter(id=_object['id']).delete()
        else:
            if _object['description'] == 'Ore':
                if _object['element_trace_assay_id_id'] == None:
                    isotope_trace = IsotopeTraceAssay.objects.get(id=_object['isotope_trace_assay_id_id'])
                    _ore = Ore(
	                    museum_number = _object['museum_number'],
	                    country = _object['country'],
	                    site = _object['site'],
	                    description = _object['description'],
	                    mineral='Chalcopyrite',
	                    source = _object['source'],
	                    isotope_trace_assay_id = isotope_trace
                    ) 
                    _ore.save()
                    Metal.objects.filter(id=_object['id']).delete()
                if _object['isotope_trace_assay_id_id'] == None:    
                    element_trace = ElementTraceAssay.objects.get(id=_object['element_trace_assay_id_id'])
                    _ore = Ore(
	                    museum_number = _object['museum_number'],
	                    country = _object['country'],
	                    site = _object['site'],
	                    description = _object['description'],
	                    mineral='Chalcopyrite',
	                    source = _object['source'],
	                    element_trace_assay_id = element_trace
                    ) 
                    _ore.save()
                    Metal.objects.filter(id=_object['id']).delete()
