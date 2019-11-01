import csv
import pdb
from apps.metal.models import IsotopeTraceAssay
from apps.metal.models import Metal


def run(*args):
    filename = args[0]
    file = csv.DictReader(open(filename))                
    for row in file:
        isotope_assay = IsotopeTraceAssay(
            # delta_copper_65=row['delta Copper 65'],
            lead_208_to_206=row['208Pb/206Pb'],
            lead_207_to_206=row['207Pb/206Pb'],
            lead_206_to_204=row['206Pb/204Pb'],
            analysis_method='Unknown'
        )
        isotope_assay.save()
        metal_artifact = Metal(
            museum_number=row['Museum or excavation No.'],
            time_period='Bronze Age',
            country=row['Country'],
            site=row['Site'],
            description=row['Description'],
            source='OXALID',
            isotope_trace_assay_id=isotope_assay
        )
        metal_artifact.save()
