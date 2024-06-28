import Encoding
import pandas as pd 
import torch as pt  
from ast import literal_eval

File = pd.read_csv("Materialsdf.csv")

File["EncodedVec"] = literal_eval(File["EncodedVec"])

# T1 = pt.Tensor(File["EncodedVec"], type=tuple)

print(File.dtypes)
