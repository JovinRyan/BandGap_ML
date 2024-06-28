import pymatgen.core as mg
import pandas as pd
import numpy as np
from pymatgen.ext.matproj import MPRester
from Encoding import CompoundEncode
from Encoding import DataFrametoDict

API = #Your API here
mpr = MPRester(API)

RelevantElementData = pd.read_csv("BandGapRelevantData.csv")
Dict = DataFrametoDict(RelevantElementData)


Data = mpr.summary.search(fields=["formula_pretty", "band_gap"])
Pretty_Formula = []
Band_Gap = []
for i in range(len(Data)):
    if "(" not in Data[i].formula_pretty:
        Pretty_Formula.append(Data[i].formula_pretty)
        Band_Gap.append(Data[i].band_gap)

EncodedData = []

for i in range(len(Pretty_Formula)):
    EncodedData.append(CompoundEncode(Pretty_Formula[i], Dict))

MaterialsDf = pd.DataFrame({"PrettyFormula" : Pretty_Formula, "Data" : EncodedData, "BandGap" : Band_Gap})

MaterialsDf = MaterialsDf.sample(frac=1)

MaterialsDf = MaterialsDf.dropna()

print(MaterialsDf.isna().sum())

MaterialsDf.to_csv("UpdatedMaterialsDF.csv", index=False)



