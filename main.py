import numpy as np
import matplotlib.pyplot as plt
from HQAM.I_8HQAM import I_8HQAM
from HQAM.I_16HQAM import  I_16HQAM
from HQAM.I_4HQAM import  I_4HQAM
from HQAM.R_16HQAM import R_16HQAM
from HQAM.R_8HQAM import R_8HQAM

from HQAM.R_4HQAM import R_4HQAM

num_symbols = 250

x_int = np.random.randint(0, 1, num_symbols)  # 0 to 1

def hasNoise():
    hasNoise = input("Constellation in the presence of additive white gaussian noise?")
    if hasNoise.lower() == "true" or hasNoise.lower()=="y"  or hasNoise.lower()=="yes" :
        return True
    if hasNoise.lower() == "false" or hasNoise.lower()=="n"  or hasNoise.lower()=="no" :
        return False
    return hasNoise

def isRegular():
    isRegular = input("Regular or Irregular constellation?")
    if isRegular.lower() == "regular" or isRegular.lower()=="r"   :
        return True
    if isRegular.lower() == "irregular"  or isRegular.lower()=="i" :
        return False
    return isRegular

M = int(input("Enter number of symbols of the constellation: ")) #M=4,8,16
if(M != -1):
    regular= isRegular()
    noise = hasNoise()

while M != -1:
    if M == 4:
        if(regular):
            R_4HQAM.__init__(x_int, np, plt, noise)
        else:
            I_4HQAM.__init__(x_int,np,plt,noise)
        M = int(input("Enter number of symbols of the constellation: "))
        if (M != -1):
            regular = isRegular()
            noise = hasNoise()
    if M == 8:
        if (regular):
            R_8HQAM.__init__(x_int, np, plt, noise)
        else:
            I_8HQAM.__init__(x_int, np, plt, noise)
        M = int(input("Enter number of symbols of the constellation:  "))
        if (M != -1):
            regular = isRegular()
            noise = hasNoise()

    if M == 16:
        if(regular):
            R_16HQAM.__init__(x_int, np, plt, noise)
        else:
            I_16HQAM.__init__(x_int, np, plt, noise)
        M = int(input("Enter number of symbols of the constellation:  "))
        if (M != -1):
            regular = isRegular()
            noise = hasNoise()




