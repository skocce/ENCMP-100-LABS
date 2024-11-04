#%% LAB 1  ENCMP 100 Computer Programming for Engineers
#
# Student name: Savelii Kosse  
# Student CCID: kosse
# Others:
#     https://www.w3schools.com/python/matplotlib_labels.asp    0%
#
#     https://www.google.com 4%
#
#
#     Savelii Kosse 91%
#
# To avoid plagiarism, list the names of others, Version 0 author(s)
# aside, whose code, words, ideas, images, or data you incorporated.
# To avoid unauthorized collaboration, list all others, excluding
# lab instructor and TAs, who gave compositional assistance.
#
# After each name, including your own name, enter in parentheses an
# estimate of the source's contributions in percent. Supply these
# numbers, which must add to 100%, to receive a nonzero mark.
#
# For obscure and anonymous or known and non-human sources, enter
# pseudonyms or names in uppercase, e.g., DARKWEB or CHATGPT, followed
# by percentages. Send one email to the lab instructor with copies of
# obscure and anonymous sources when you submit your assignment.
#
#%% HSPECTRUM  Quantum Chemistry and the Hydrogen Emission Spectrum
#
# The periodic table is central to chemistry. According to Britannica,
# "Detailed understanding of the periodic system has developed along with
# the quantum theory of spectra and the electronic structure of atoms,
# beginning with the work of Bohr in 1913." In this lab assignment, a
# University of Alberta student explores the Bohr model's accuracy in
# predicting the hydrogen emission spectrum, using observed wavelengths
# from a US National Institute of Standards and Technology database.
#
# Copyright (c) 2024, University of Alberta
# Electrical and Computer Engineering
# All rights reserved.
#
import numpy as np
import matplotlib.pyplot as plt

#%% EXPERIMENT DATA
#
data = [656.460, 486.271, 434.1692, 410.2892, 397.1198, 389.0166, 383.6485] # nm
nist = np.array(data)
n = len(nist)


# 1. State variables for Bohr. Calculate Bohr value 'R' using formula.
# 2. Find wavelength 'wave' using the formula provided and Bohr value found earlier
# 3. Find new R using by multiplying R before by a constant formula involving mass of protons and electrons
# 4. Find absolute value of all numbers in the list and then find the biggest value and print it.
# convert wavelength from m to nm 
# 5. 
#%% MODEL SETUP
#
me = 9.1093837e-31    #kg
e = 1.602176634e-19  # Coulomb
E = 8.85418782e-12 #F/m
h = 6.62607015e-34 #Js
c = 299792458 #m/s

mp = 1.6726219e-27 #kg

den = me*e**4

num = 8*(E**2)*(h**3)*c

R=den/num


NEWR = R*(mp/(mp+me))


#R = 1.0973732e7 # 1/m
print("Rydberg constant:", int(NEWR) , '1/m')

nf = int(input("Final state (nf): "))
ni = np.arange(nf + 1, nf + n + 1)

brackets = (1/nf**2)-(1/ni**2)
mul = R * brackets

wave = 1/mul

wavenm = wave *1.0e9

#print(wavenm)

SBar = 1/(NEWR * brackets)

wavenm2 = SBar * 1.0e9

WPE =  nist - wavenm2

absw = np.abs(WPE)

maxw = np.max(absw)

#print(absw)
print("Worst-case error: " ,"%.3f" % maxw , 'nm')

#1. Plot lists given 'data' as croses and plot list 'wavenm' as red dots with size '3'
#2. Add x and y labels, Title, and legend
#%% SIMULATION DATA
#

plt.plot(ni, nist, 'bx', label='NIST data')
plt.plot(ni, wavenm, 'ro', label='Bohr model', markersize=3)
plt.grid(True)
plt.legend()

plt.title("Hydrogen Emission Spectrum")
plt.ylabel("Wavelength nm")
plt.xlabel("Initial state ni")



plt.show()


# 1. Plot list made 'error' bars with a color magenta 
# 2. and then we plot another bar gragh using WorstPossivleError (WPE)
#%% ERROR ANALYSIS

error = nist - wavenm

# Plotting the first bar graph (NIST-Bohr differences)
plt.bar(ni, error, color='magenta', label='NIST-Bohr')
plt.xlabel('Initial state (ni)')
plt.ylabel('Wavelength (nm)')
plt.title('Hydrogen Emission Spectrum')
plt.legend()
plt.show()



# Plotting the first bar graph (NIST-Bohr differences)
plt.bar(ni, WPE, color='magenta', label='NIST-Bohr')
plt.xlabel('Initial state (ni)')
plt.ylabel('Wavelength (nm)')
plt.title('Hydrogen Emission Spectrum')
plt.legend()
plt.show()





