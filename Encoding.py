import pandas as pd

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]  #All lowercase letters (listed to convert ["H", "e"] -> ["He"])
Elements = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne",
            "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar",
            "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr",
            "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe",
            "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn",
            "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og",] #List of Elements


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
    return InpString                                            #Ex Input: "H2O" Output: ["H", "2", "O"]
                                                                #   Input: "NaOH" Output: ["Na", "O", "H"]

def ParenthesesRemover(InCompound=list):                        #Should help increase datapoints
    if "(" not in InCompound:
        return InCompound

    else:
        StartIndex = InCompound.index("(")
        StopIndex = InCompound.index(")")
        Stoich = InCompound[StopIndex+1]
        List = InCompound[StartIndex+1:StopIndex-1]
        for item in List:
            if item in Elements:
                List.insert(List.index(item)+1, Stoich)
        InCompound[StartIndex+1:StopIndex-1] = List
        InCompound = InCompound[:-1]
        InCompound.remove("(")
        InCompound.remove(")")
        for i in range(len(InCompound) - 1, -1, -1):
            if isfloat(InCompound[i]) and isfloat(InCompound[i-1]):
                InCompound[i-1] = str(int(InCompound[i-1]) * int(InCompound[i]))
                InCompound.pop(i)

        return InCompound

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

def ElementalPropertyEncoder(ElementList: list, CoordList: list, Propertydf: dict = ElementDataDict):
    PropertiesList = []
    for i in range(len(ElementList)):
        Properties = Propertydf[ElementList[i]]
        PropertiesList.append(Properties)

    # for j in range(len(PropertiesList)):
    #     for k in range(len(PropertiesList[j])):
    #         PropertiesList[j][k] = PropertiesList[j][k]*CoordList[j]

    # return PropertiesList
    TempList = []
    for j in range(len(PropertiesList)):
        for k in range(len(PropertiesList[j])):
            TempList.append(PropertiesList[j][k]*CoordList[j])

    Temp_2 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    for i in range(len(TempList)):
        Temp_2[i%7] += TempList[i]

    return Temp_2

def CompoundEncode(Compound: str, DataDict = ElementDataDict):  #Quite a convoluted way to collect all the functions but it works :>
    SplitList = ElementEncoding(Compound)
    SplitList = ParenthesesRemover(SplitList)
    ElementList, CoordList = StoichEncoding(SplitList)
    EncodedDat =  ElementalPropertyEncoder(ElementList, CoordList, DataDict)
    return EncodedDat


