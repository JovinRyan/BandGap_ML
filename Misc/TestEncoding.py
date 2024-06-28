letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
Elements = ["H", "He",
               "Li", "Be", "B", "C", "N", "O", "F", "Ne",
               "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar",
               "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr",
               "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe",
               "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn",
               "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og",]
ExCompound  = "12345"

def isfloat(x):
    try:
        float(x)
        return True
    except:
        return False

def CompoundID(Compound):
    Compound = [*Compound]
    for i in range(len(Compound)):
        try:
            if Compound[i+1] in letters:
                Compound[i] = Compound[i] + Compound[i+1]
                Compound.pop(i+1) 
        except:
            continue
        # try:
        #     if (isfloat(Compound[i]) and isfloat(Compound[i+1])) and isfloat(Compound[i+2]):
        #         print("triple")
        #         Compound[i] = float(Compound[i] + Compound[i+1] + Compound[i+2])
        #         Compound.pop(i+1)
        #         Compound.pop(i+1)
        # except:
        #     continue
        try:
            if isfloat(Compound[i]) and isfloat(Compound[i+1]):
                print("double")
                Compound[i] = float(Compound[i] + Compound[i+1])
                Compound.pop(i+1)
        except:
            continue
        try:
            if isfloat(Compound[i]):
                print("single")
                Compound[i] = float(Compound[i])
        except:
            continue
    return Compound

def StoichAggregator(InpList: list):
    numericstring = []
    for i in range(len(InpList)):
        while isfloat(InpList[i]):
            numericstring.append(i)
            if i == len(numericstring) - 1:
                break
            else:
                i+=1
        print(numericstring)
  
    


def StoichEncode(Compound: list):
    StoichList = []
    ElementList = []
    for i in range(len(Compound)):
        if isfloat(Compound[i]):
            StoichList.append(Compound[i])
            StoichList.pop(i-1)
        elif isinstance(Compound[i], str):
            ElementList.append(Compound[i])
            StoichList.append(1.0)
    StoichSum = sum(StoichList)
    for i in range(len(StoichList)):
        StoichList[i] = StoichList[i]/StoichSum
    return ElementList, StoichList
            
            

def Encode(Compound: list):
    Compound = CompoundID(Compound)
    print(Compound, len(Compound))
    CompoundData = StoichEncode(Compound)
    return CompoundData

# print(CompoundID(ExCompound))

Test = ["C", "H", "1", "2", "3", "4"]
testlist = []
i=0
for i in range(len(Test)):
    if isfloat(Test[i]):
        testlist.append(Test[i])
    else:
        continue
            
def Stoich(InpList: list):
    StoichList = []
    for i in range(len(InpList)):
        templist =[]
        while isfloat(InpList[i]):
            templist.append(InpList[i])
            i += 1