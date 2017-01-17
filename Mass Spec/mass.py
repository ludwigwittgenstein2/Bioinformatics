#!/usr/bin/python
#Mass Spec Prototype v.0.1
#Rick Rejeleene
#problems so far - Isoleucine, Leucine having same formula
#How to declare aminoacids in a single letter when there is Glutamine & Glycine with the same letters
#Need to find a way to find possible masses


#Isotopic masses and their abundance
C12 = { 'Mass' : 12, 'Percentage' : 98.99 }
C13 = { 'Mass' : 13.0035,'Percentage' : 1.1 }
N14 = { 'Mass' : 14.003074,'Percentage' : 99.632 }
N15 =  { 'Mass' : 15.000108 ,'Percentage' : 0.368 }
H1 = { 'Mass' : 1.007825,'Percentage' : 99.99 }
H2 = { 'Mass' : 2.014102,'Percentage' : 0.015 }
O16 = { 'Mass' : 15.994915,'Percentage' : 99.76 }
O17 = { 'Mass' : 16.999131,'Percentage' : 0.038 }
O18 = { 'Mass' : 17.999159,'Percentage' : 0.2 }
S32 = {'Mass':31.972072,'Percentage':95.02}
S33 = {'Mass':32.971459,'Percentage':0.75}
S34 = {'Mass':33.967868,'Percentage':4.21}
S36 = {'Mass':35.967079,'Percentage' :0.020}


C6H13NO2 = (C12,C12,C12,C12,C12,C13,H1,H1,H1,H1,H1,H1,H1,H1,H1,H1,H1,H1,H2,N14,O16,O17)
C6H14N2O2 = (C12,C12,C12,C12,C12,C13,H1,H1,H1,H1,H1,H1,H1,H1,H1,H1,H1,H1,H1,H2,N14,N15,O16,O17)
C5H11NO2S =(C12,C12,C12,C12,C13,H1,H1,H1,H1,H1,H1,H1,H1,H1,H1,H2,N14,O16,O17,S32)
C9H11NO2 = (C12,C12,C12,C12,C12,C12,C12,C12,C13,H1,H1,H1,H1,H1,H1,H1,H1,H1,H1,H2,N14,O16,O17)
C4H9NO3 =(C12,C12,C12,C13,H1,H1,H1,H1,H1,H1,H1,H1,H2,N14,O16,O17,O18)
C11H12N2O2 =(C12,C12,C12,C12,C12,C12,C12,C12,C12,C13,H1,H1,H1,H1,H1,H1,H1,H1,H1,H1,H1,H2,N14,N15,O16,O17)
C5H11NO2 = (C12,C12,C12,C12,C13,H1,H1,H1,H1,H1,H1,H1,H1,H1,H1,H2,N14,O16,O17)
C6H14N4O2= (C12,C12,C12,C12,C12,C13,H1,H1,H1,H1,H1,H1,H1,H1,H1,H1,H1,H1,H1,H2,N14,N14,N14,N15,O16,O17)
C6H9N3O2= (C12,C12,C12,C12,C12,C13,H1,H1,H1,H1,H1,H1,H1,H1,H2,N14,N14,N15,O16,O17)
C3H7NO2 = (C12,C12,C13,H1,H1,H1,H1,H1,H1,H2,N14,O16,O17)
C4H8N2O3 = (C12,C12,C12,C13,H1,H1,H1,H1,H1,H1,H1,H2,N14,N15,O16,O17,O18)
C4H7NO4 = (C12,C12,C12,C13,H1,H1,H1,H1,H1,H1,H2,N14,O16,O16,O17,O18)
C3H7NO2S= (C12,C12,C13,H1,H1,H1,H1,H1,H1,H2,N14,O16,O17,S32)
C5H9NO4 = (C12,C12,C12,C12,C13,H1,H1,H1,H1,H1,H1,H1,H1,H2,N14,O16,O16,O17,O18)
C5H10N2O3 = (C12,C12,C12,C12,C13,H1,H1,H1,H1,H1,H1,H1,H1,H1,H2,N14,N15,O16,O17,O18)
C2H5NO2 = (C12,C13,H1,H1,H1,H1,H2,N14,O16,O17)
C5H9NO2 = (C12,C12,C12,C13,C13,H1,H1,H1,H1,H1,H1,H1,H1,H2,N14,O16,O17)
C3H7NO3 = (C12,C12,C13,H1,H1,H1,H1,H1,H1,H2,N14,O16,O17,O18)
C9H11NO3 = (C12,C12,C12,C12,C12,C12,C12,C13,H1,H1,H1,H1,H1,H1,H1,H1,H1,H1,H2,N14,O16,O17,O18)




#amino acids and their molecular formulas	
aminoacid = {'Isoleucine': C6H13NO2,'Leucine': C6H13NO2,'Lysine': C6H14N2O2,'Methionine': C5H11NO2S,
'Phenylalanine': C9H11NO2,'Threonine': C4H9NO3,'Tryptophan': C11H12N2O2,'Valine': C5H11NO2,
'Arginine': C6H14N4O2,'Histidine': C6H9N3O2,'Alanine': C3H7NO2,'Asparagine': C4H8N2O3,
'Aspartate': C4H7NO4,'Cysteine': C3H7NO2S,'Glutamate': C5H9NO4,'Glutamine': C5H10N2O3,'Glycine': C2H5NO2,
'Proline': C5H9NO2,'Serine': C3H7NO3,'Tyrosine': C9H11NO3}




def total_mass(molecule):
	return sum(a['Mass'] for a in molecule)
	

input = raw_input("Get the User value \n")

if input in aminoacid:
    molecule = aminoacid[input]
    print "The Mass is \n" + str(total_mass(molecule))
    
    
    
    
    
    
 #--I-Isoleucine
#--L-Leucine
#--K-Lysine
#--M-Methionine
#--F-Phenylalanine
#--T-Threonine
#--W-Tryptophan
#--V-Valine
#--R-Arginine
#--H-Histidine
#--A-Alanine:
#--N-Asparagine
#--D-Aspartate
#--C-Cysteine
#--E-Glutamate
#--Q-Glutamine
#--G-Glycine
#--P-Proline
#--S-Serine
#--T-Tyrosine   


