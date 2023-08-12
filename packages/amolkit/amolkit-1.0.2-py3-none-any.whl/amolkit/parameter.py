from collections import OrderedDict
from amolkit.stringmanip import getPenaltyfromString

def readCharmmParameter(parfile):
    """
    Get Charmm parameters from any file containing parameters.
    Arguments:
        parfile: It can be any file format containing charmm parameters in correct style.
    Returns:
        parameters: Dictionary with keywords BONDS, ANGLES, DIHEDRALS and IMPROPERS
                    Example: parameter["BONDS"] = [[attyp1,attyp2,kval,eqdist],...]
                    Example: parameter["ANGLES"] = [[attyp1,attyp2,attyp3,kval,eqangl],...]
                    Example: parameter["DIHEDRALS"] = [[attyp1,attyp2,attyp3,attyp4,kval,mult,eqangl],...]
    Note:
        Have to add extraction of vdw parameters.
        Canonicalization of parameters need to be performed from a separate function. 
        Because user may be reading multiple files using this function. 
        User should latter canonicalize and only keep unique parameters.
    """

    parameters={}
    for marker in ["BONDS","ANGLES","DIHEDRALS","IMPROPERS"]:
        parameters[marker] = [] 

    marker = ""
    with open(parfile,'r') as readpar:
        for line in readpar:
            field = line.strip().split("!")[0].split()
            comment = "!".join(line.strip().split("!")[1:])
            if len(field) > 0:
                if len(field) == 1:
                    if field[0].upper() == "BONDS":
                        marker = "BONDS"
                    if field[0].upper() == "ANGLES":
                        marker = "ANGLES"
                    if field[0].upper() == "DIHEDRALS":
                        marker = "DIHEDRALS"
                    if field[0].upper() == "IMPROPER":
                        marker = "IMPROPERS"
                try:
                    if marker in ["BONDS","ANGLES","DIHEDRALS","IMPROPERS"]:
                        penalty,comment = getPenaltyfromString(comment)
                    if marker == "BONDS" and len(field) == 4:
                        parameters[marker].append([field[0],field[1],round(float(field[2]),4),round(float(field[3]),4),penalty,comment])
                    if marker == "ANGLES" and len(field) == 5:
                        parameters[marker].append([field[0],field[1],field[2],round(float(field[3]),4),round(float(field[4]),4),penalty,comment])
                    if marker == "ANGLES" and len(field) == 7:
                        parameters[marker].append([field[0],field[1],field[2],round(float(field[3]),4),round(float(field[4]),4),round(float(field[5]),4),round(float(field[6]),4),penalty,comment])
                    if marker in ["DIHEDRALS","IMPROPERS"] and len(field) == 7:
                        parameters[marker].append([field[0],field[1],field[2],field[3],round(float(field[4]),4),int(field[5]),round(float(field[6]),1),penalty,comment])
                except (ValueError,IndexError):
                    pass
    return parameters

def readCharmmParameterFiles(parfiles:list):
    """
    Get Charmm parameters from multiple files and collect in parameters dictionary
    Arguments:
       parfiles: list of files containing charmm parameters
    Returns:
       parameters: Dictionary containing all parameters obtained from list in parfiles
    """

    if isinstance(parfiles,str):
        parfiles=[parfiles]

    parameters={}
    for marker in ["BONDS","ANGLES","DIHEDRALS","IMPROPERS"]:
        parameters[marker] = [] 

    for parfile in parfiles:
        cparams = readCharmmParameter(parfile)
        for key,value in cparams.items():
            if not parameters[key]: 
               parameters[key] = cparams[key]
            else:
               parameters[key].append(cparams[key])
    return parameters           

def canonical_format(iclist,icnumlist):
    # Horizontal swapping using ranking scheme
    for i in range(len(iclist)):
        if len(iclist[i]) == 2:
           ric1,ric2= ranking(iclist[i][0],iclist[i][1])
           if ric1 > ric2:
              iclist[i] = iclist[i][::-1]
              icnumlist[i] = icnumlist[i][::-1]
              
        if len(iclist[i]) == 3:
           ric1,ric2 = ranking(iclist[i][0],iclist[i][2])
           if ric1 > ric2:
              iclist[i] = iclist[i][::-1]
              icnumlist[i] = icnumlist[i][::-1]

        if len(iclist[i]) == 4:
           ric1,ric2 = ranking(iclist[i][0],iclist[i][3])
           if ric1 > ric2:
              iclist[i] = iclist[i][::-1]
              icnumlist[i] = icnumlist[i][::-1]
              
    # Vertical swapping using alphabetical order
    iclist = [i for i in sorted(iclist, key=lambda ic:ic[0])]
    icnumlist = [i for _,i in sorted(zip(iclist,icnumlist), key=lambda ic:ic[0][0])]
    return(iclist,icnumlist)

def ranking(atnm1,atnm2):
    # If in future new elements are added to rank dict then forced ranking 11 and 12 
    # should change accordingly.
    rank={"C":1,"N":2,"O":3,"P":4,"S":5,"F":6,"CL":7,"BR":8,"B":9,"AL":10,"H":30}
    ratnm1 = rank.get(atnm1[0:2].upper())
    if ratnm1 == None: ratnm1 = rank.get(atnm1[0:1].upper())
    ratnm2 = rank.get(atnm2[0:2].upper())
    if ratnm2 == None: ratnm2 = rank.get(atnm2[0:1].upper())
    if ratnm1 == None and ratnm2 == None:
        #if ratnm1 > ratnm2:
        ratnm1 = 11 
        ratnm2 = 12
        #else:
        #    ratnm1 = 12 
        #    ratnm2 = 11
    elif ratnm1 == None and ratnm2 != None:
        ratnm1 = 11
    elif ratnm1 != None and ratnm2 == None:
        ratnm2 = 11
    return (ratnm1,ratnm2)     

class Parameter():
    def __init__(self):
        """
        Constructor for the Parameter class.
        """

    def loadCharmmParameter(self,parfiles):
        """
        Load topology information using CHARMM force field and store it as attributes.

        Args:
            resname (str): Name of the residue.
            resitopfile (str): Path to the CHARMM topology file.
        """

        self.charmmParameter = readCharmmParameterFiles(parfiles)
