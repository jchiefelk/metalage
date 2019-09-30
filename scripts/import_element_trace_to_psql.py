import os
import csv
from apps.metal.models import Metal
from apps.metal.models import ElementTraceAssay


def run(*args):
    filename = args[0]
    element_trace_assay_id = ''
    source = ''
    country = ''
    description = ''
    time_period = 'Bronze Age'
    site = '' 
    file = csv.DictReader(open(filename))                
    for row in file:
        trace_assay= ElementTraceAssay(
        	analysis_method=row['Method of analysis'],
            gold_ppm=row['Au(ppm)'],
            arsenic_percent=row['As(%)'],
            # antimony_percent=row['Sb(%)'],
            #arsenic_ppm=row['As(ppm)'],
            antimony_ppm=row['Sb(ppm)'],
            #selenium_ppm=row['Se(ppm)'],
            # selenium_percent=row['Se(%)'],
            # tellurium_percent=row['Ag(%)'],
            #silver_percent=row['Ag(%)'],
            silver_ppm=row['Ag(ppm)'],
            # tin_percent=row['Sn(%)'],
            #tin_ppm=row['Sn(ppm)'],
            # zinc_percent=row['Zn(%)'],
            zinc_ppm=row['Zn(ppm)'],
            #cobalt_ppm=row['Co(ppm)'],
            cobalt_percent=row['Co(%)'],
            nickel_percent=row['Ni(%)'],
            #nickel_ppm=row['Ni(ppm)'],
            # lead_percent=row['Pb(%)'],
            #lead_ppm=row['Pb(ppm)'],
            chromium_percent=row['Cr(%)'],
            #copper_ppm=row['Cu(ppm)'],
            #iron_ppm=row['Fe(ppm)'],
            # sodium_ppm=row['Na'],
            # magnesium_ppm=row['Mg'],
            #aluminum_ppm=row['Al(ppm)'],
            # silicon_ppm=row['Si'],
            # phosphorous_ppm=row['P'],
            # sulfur_ppm=row['S'],
            # scandium_ppm=row['Sc'],
            # titanium_ppm=row['Ti'],
            # vanadium_ppm=row['V'],
            # chromium_ppm=row['Cr'],
            #manganese_ppm=row['Mn(ppm)'],
            # molybdenum_ppm=row['Mo'],
            # rhodium_ppm=row['Rh'],
            #cadmium_ppm=row['Cd(ppm)'],
            #indium_ppm=row['In(ppm)'],
            #tellurium_ppm=row['Te(ppm)'],
            # lanthanum_ppm=row['La'],
            # cerium_ppm=row['Ce'],
            # tantalum_ppm=row['Ta'],
            # platinum_ppm=row['Pt'],
            # mercury_ppm=row['Hg'],
            #bismuth_ppm=row['Bi(ppm)'],
            # bismuth_percent=row['Bi(%)'],
            # uranium_ppm=row['U']                        
            copper_percent=row['Cu(%)'],
            #sulfur_percent=row['S(%)'],
            iron_percent=row['Fe(%)']
        )
        trace_assay.save()
        _metal = Metal(
	        museum_number=row['Museum or excavation No.'],
	        time_period='Bronze Age',
	        country=row['Country'],
	        site=row['Site'],
	        description=row['Description'],
	        source=row['Source (DOI)'],
	        element_trace_assay_id=trace_assay
        )
        _metal.save()
