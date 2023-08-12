import os,sys
import amolkit 
from collections import OrderedDict

def test_readaddi():
    from amolkit.topology import readCharmmTopology
    
    allinfo=open("readaddi.txt","r").readlines()
    
    for e in allinfo:
        a=e.split()
        top=readCharmmTopology(a[0],a[1])
        assert top["rescharge"] == float(a[2])

def test_readdrud():
    from amolkit.topology import readCharmmTopology
    allinfo=open("readdrud.txt","r").readlines()
    
    for e in allinfo:
        a=e.split()
        top=readCharmmTopology(a[0],a[1])
        assert top["rescharge"] == float(a[2])

def test_genpsf_readaddi():
    from amolkit.topology import readCharmmTopology
    from amolkit.topology import Topology
    from amolkit.topology import Psf
    
    t=Topology()
    t.loadCharmmTopology("ACET","readaddi/top_all36_cgenff.rtf")
    p=Psf(t)
    p.genpsf()
    npsfatoms = 7
    print (p.npsfatoms)
    assert p.npsfatoms == npsfatoms

def test_genpsf_readdrud():
    from amolkit.topology import readCharmmTopology
    from amolkit.topology import Topology
    from amolkit.topology import Psf
    
    t=Topology()
    t.loadCharmmTopology("ALAD","readdrud/toppar_drude_master_protein_2019g.str")
    p=Psf(t)
    p.genpsf()
    npsfatoms = 36
    print (p.npsfatoms)
    assert p.npsfatoms == npsfatoms

def test_genpsf_mainaddi():
    from amolkit.topology import readCharmmTopology
    from amolkit.topology import Topology
    from amolkit.topology import Psf
    
    t=Topology()
    t.loadCharmmTopology("OXAZ","mainaddi/oxaz.str")
    p=Psf(t)
    p.genpsf()
    npsfatoms = 11
    print (p.npsfatoms)
    assert p.npsfatoms == npsfatoms

def test_genpsf_maindrud():
    from amolkit.topology import readCharmmTopology
    from amolkit.topology import Topology
    from amolkit.topology import Psf
    
    t=Topology()
    t.loadCharmmTopology("OXAZ","maindrud/oxaz.str")
    p=Psf(t)
    p.genpsf()
    npsfatoms = 11
    print (p.npsfatoms)
    assert p.npsfatoms == npsfatoms

def test_molsystem(tmp_path):
    from amolkit.molecule import Molecule
    from amolkit.molecule import writepdb
    from amolkit.molsystem import MolSystem
    
    resn=MolSystem()
    resn.loadTopology("OXAZ","mainaddi/oxaz.str")
    resn.loadParameters("mainaddi/oxaz.str")
    bondparam=[['C1', 'C2', None, None, None], ['C1', 'N', None, None, None], 
            ['C1', 'H1', None, None, None], ['C1', 'H2', None, None, None], 
            ['C2', 'O1', None, None, None], ['C2', 'H3', None, None, None], 
            ['C2', 'H4', None, None, None], ['O1', 'C3', None, None, None], 
            ['C3', 'O2', None, None, None], ['C3', 'N', None, None, None], 
            ['N', 'H5', None, None, None]]
    angleparam=[['C2', 'C1', 'N', None, None, None], ['C2', 'C1', 'H1', None, None, None], 
            ['C2', 'C1', 'H2', None, None, None], ['N', 'C1', 'H1', None, None, None], 
            ['N', 'C1', 'H2', None, None, None], ['H1', 'C1', 'H2', None, None, None], 
            ['C1', 'C2', 'O1', None, None, None], ['C1', 'C2', 'H3', None, None, None], 
            ['C1', 'C2', 'H4', None, None, None], ['O1', 'C2', 'H3', None, None, None], 
            ['O1', 'C2', 'H4', None, None, None], ['H3', 'C2', 'H4', None, None, None], 
            ['C2', 'O1', 'C3', None, None, None], ['O1', 'C3', 'O2', None, None, None], 
            ['O1', 'C3', 'N', 65.5, 105.0, 48.5], ['O2', 'C3', 'N', None, None, None], 
            ['C3', 'N', 'C1', None, None, None], ['C3', 'N', 'H5', None, None, None], 
            ['C1', 'N', 'H5', None, None, None]]
    dihedralparam=[['C1', 'N', 'C3', 'O1', 2, 0.4, 180.0, 68.0], 
            ['C2', 'O1', 'C3', 'N', 2, 1.24, 180.0, 48.5], 
            ['C2', 'O1', 'C3', 'N', 3, 2.27, 180.0, 48.5], 
            ['O1', 'C2', 'C1', 'N', 3, 0.2, 0.0, 32.0], 
            ['O1', 'C3', 'N', 'H5', 2, 1.27, 180.0, 68.0]]

    assert resn.bondparam == bondparam
    assert resn.angleparam == angleparam
    assert resn.dihedralparam == dihedralparam
    
    mol = Molecule() 
    mol.readmol2("mainaddi/oxaz.mol2")

    resn.loadGeometry(mol) 
    
    outfile = tmp_path + "/oxaz.pdb" 
    writepdb(resn,outfile)

    with open("mainaddi/oxaz_akit.pdb", 'rb') as file1:
        content1 = file1.read()

    with open(outfile, 'rb') as file2:
        content2 = file2.read()

    assert content1 == content2

def test_genbond_mol():
    from amolkit.molecule import Molecule
    mol=Molecule()
    mol.readxyz("readcoor/gluc.xyz")
    mol.genBonds()
    bonds = [[1, 2], [1, 7], [1, 11], [2, 1], [2, 3], [2, 8], [3, 2], [3, 4], [3, 9], 
            [4, 3], [4, 5], [4, 10], [5, 4], [5, 6], [5, 11], [6, 5], [6, 12], [7, 1], 
            [8, 2], [9, 3], [10, 4], [11, 1], [11, 5], [12, 6]]
    
    print(mol.bondindices) 
    assert mol.bondindices == bonds

def test_readcrd():
    from amolkit.molecule import Molecule
    mol=Molecule()
    mol.readcrd("readcoor/meoh.crd")
    print (mol.atomcoord_byIdx)
    atomcoord = OrderedDict([(1, [0.986, 0.015, 0.101]), (2, [2.402, 0.01, 0.091]), 
        (3, [0.625, 1.046, 0.065]), (4, [0.625, -0.478, 1.006]), 
        (5, [0.623, -0.526, -0.776]), (6, [2.694, 0.497, 0.88])])
    assert mol.atomcoord_byIdx == atomcoord

def test_readpdb():
    from amolkit.molecule import Molecule
    mol=Molecule()
    mol.readpdb("readcoor/meoh.pdb")
    atomcoord = OrderedDict([(1, [0.986, 0.015, 0.101]), (2, [2.402, 0.01, 0.091]), 
        (3, [0.625, 1.046, 0.065]), (4, [0.625, -0.478, 1.006]), 
        (5, [0.623, -0.526, -0.776]), (6, [2.694, 0.497, 0.88])])
    print (mol.atomcoord_byIdx)
    assert mol.atomcoord_byIdx == atomcoord

def test_writecrd(tmp_path):
    from amolkit.molecule import Molecule
    from amolkit.molecule import writecrd
    mol=Molecule()
    mol.readcrd("readcoor/meoh.crd")
    outfile = tmp_path + "/meoh.crd" 
    writecrd(mol,outfile)
    #writecrd(mol,tmp_path+"/meoh.crd")

    with open("readcoor/meoh_akit.crd", 'rb') as file1:
        content1 = file1.read()

    #with open(tmp_path"/meoh.crd", 'rb') as file2:
    with open(outfile, 'rb') as file2:
        content2 = file2.read()

    assert content1 == content2

def test_writepdb(tmp_path):
    from amolkit.molecule import Molecule
    from amolkit.molecule import writepdb
    mol=Molecule()
    mol.readpdb("readcoor/meoh.pdb")
    outfile = tmp_path + "/meoh.pdb" 
    writepdb(mol,outfile)
    #writepdb(mol,tmp_path"/meoh.pdb")

    with open("readcoor/meoh_akit.pdb", 'rb') as file1:
        content1 = file1.read()

    #with open(tmp_path"/meoh.pdb", 'rb') as file2:
    with open(outfile, 'rb') as file2:
        content2 = file2.read()

    assert content1 == content2

def test_writexyz(tmp_path):
    from amolkit.molecule import Molecule
    from amolkit.molecule import writexyz
    mol=Molecule()
    mol.readpdb("readcoor/meoh.pdb")
    outfile = tmp_path +"/meoh.xyz" 
    writexyz(mol,outfile) 
    #writexyz(mol,tmp_path"/meoh.xyz")

    with open("readcoor/meoh_akit.xyz", 'rb') as file1:
        content1 = file1.read()

    #with open(tmp_path"/meoh.xyz", 'rb') as file2:
    with open(outfile, 'rb') as file2:
        content2 = file2.read()

    assert content1 == content2

if __name__ == "__main__":
    tmp_path=sys.argv[1]
    test_readaddi()
    test_readdrud()
    test_genpsf_readaddi()
    test_genpsf_readdrud()
    test_genpsf_mainaddi()
    test_genpsf_maindrud()
    test_molsystem(tmp_path)
    test_genbond_mol()
    test_readcrd()
    test_readpdb()
    test_writecrd(tmp_path)
    test_writepdb(tmp_path)
    test_writexyz(tmp_path)

