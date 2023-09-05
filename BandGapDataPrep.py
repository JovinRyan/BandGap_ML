import pymatgen.core as mg 
import pandas as pd 
import numpy as np 
from pymatgen.ext.matproj import MPRester
from Encoding import CompoundEncode
from Encoding import DataFrametoDict

API = "NveUd5bVmDxgvXaXurxu18aj8QIUK9vd"
mpr = MPRester(API)

RelevantElementData = pd.read_csv("BandGapRelevantData.csv")
Dict = DataFrametoDict(RelevantElementData)


Data = mpr.summary.search(fields=["formula_pretty", "band_gap"], band_gap=(0, 0.5))
Pretty_Formula = []
Band_Gap = []
for i in range(len(Data)):
    if "(" not in Data[i].formula_pretty:
        Pretty_Formula.append(Data[i].formula_pretty)
        Band_Gap.append(Data[i].band_gap)

EncodedData = []

for i in range(len(Pretty_Formula)):
    EncodedData.append(CompoundEncode(Pretty_Formula[i], Dict))
        
MaterialsDf = pd.DataFrame([Pretty_Formula, EncodedData, Band_Gap])

MaterialsDf = MaterialsDf.T

MaterialsDf.to_csv("Materialsdf3.csv", index=False)

