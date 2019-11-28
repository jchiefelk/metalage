from apps.metal.models import ElementTraceAssay
from apps.metal.models import IsotopeTraceAssay
from apps.metal.models import Metal


def run(*args):
    element_trace_list = {}
    isotope_trace_list = {}
    metal_objects =  Metal.objects.all().values('element_trace_assay_id_id', 'isotope_trace_assay_id_id')
    for _object in metal_objects:
        if _object['isotope_trace_assay_id_id']:
            isotope_trace_list[_object['isotope_trace_assay_id_id']] = None

        if _object['element_trace_assay_id_id']:
            element_trace_list[_object['element_trace_assay_id_id']] = None

    
    element_trace_ids = ElementTraceAssay.objects.all().values('id')
    for _object in element_trace_ids:
        if _object['id'] in element_trace_list:
            continue
        else:
            data_set = ElementTraceAssay.objects.filter(id=_object['id'])
            data_set.delete()

    
    isotope_trace_ids = IsotopeTraceAssay.objects.all().values('id')
    for _object in isotope_trace_ids:
        if _object['id'] in isotope_trace_list:
            continue
        else:
            data_set = IsotopeTraceAssay.objects.filter(id=_object['id'])
            data_set.delete()
