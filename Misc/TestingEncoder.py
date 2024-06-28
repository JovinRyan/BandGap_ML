import pandas as pd

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
Elements = ["H", "He",
               "Li", "Be", "B", "C", "N", "O", "F", "Ne",
               "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar",
               "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr",
               "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe",
               "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn",
               "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og",]


RelevantElementData = pd.read_csv("BandGapRelevantData.csv")

def DataFrametoDict(df = RelevantElementData, SymbolCol = "Symbol"):
    ElementDataDict = df.set_index(SymbolCol).T.to_dict('list')
    return ElementDataDict

ElementDataDict = DataFrametoDict()

def isfloat(x):
    try:
        float(x)
        return True
    except:
        return False
    
def ElementEncoding(InpString: str):
    InpString = [*InpString]
    for i in range(len(InpString)):
        try:
            if InpString[i+1] in letters:
                InpString[i] = InpString[i] + InpString[i+1]
                InpString.pop(i+1) 
        except:
            break
    return InpString   

def StoichEncoding(InpList: list):
    NumericList = []
    StrList = []
    for i in range(len(InpList)):
        if isfloat(InpList[i]):
            NumericList.append(InpList[i])
        else:
            StrList.append(InpList[i])
            NumericList.append("x")
    NumericStr = "".join(NumericList)
    NumericStr = NumericStr.replace("x", ",")
    NumericList = NumericStr.split(",")
    for i in range(len(NumericList)):
        if NumericList[i] == "":
            NumericList[i] = "1"
        NumericList[i] = float(NumericList[i])
    NumericList.pop(0)                                          #I don't know why but a "1" is added to the list which needs to be popped
    stoichsum = sum(NumericList)
    for i in range(len(NumericList)):
        NumericList[i] = NumericList[i]/stoichsum
    
    return StrList, NumericList

def ElementalPropertyEncoder(ElementList: list, CoordList: list, Propertydf = ElementDataDict):
    PropertiesList = []
    for i in range(len(ElementList)):
        Properties = Propertydf[ElementList[i]]
        PropertiesList.append(Properties)
    
    TempList = []
    for j in range(len(PropertiesList)):
        for k in range(len(PropertiesList[j])):
            TempList.append(PropertiesList[j][k]*CoordList[j])

    Temp_2 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    for i in range(len(TempList)):
        Temp_2[i%7] += TempList[i]

    return Temp_2

CompoundList = ["Fe10F19","Fe10F19","Fe10F19","Fe10F19"]
#CompoundList = ["Fe10F19", "K2NaRhF6", "Cs4FeO4", "Li3V4O11F"]


# for i in range(len(CompoundList)):
#     print(StoichEncoding(ElementEncoding(CompoundList[i])))

for i in range(len(CompoundList)):
    print(ElementalPropertyEncoder(StoichEncoding(ElementEncoding(CompoundList[i]))[0], StoichEncoding(ElementEncoding(CompoundList[i]))[1]))

# for i in range(len(CompoundList)):
#     print(ElementEncoding(CompoundList[i]))