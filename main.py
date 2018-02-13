#!/usr/bin/python

import scipy.constants as cs
import numpy as np
from funct import *
from integrator import *
from sys import argv 
import barmat
from time import time

import matplotlib.pyplot as plt 


if __name__ == '__main__':

    start = time()
    step = argv[1]
    
    t = 0.1  #in K
    tc = 1.3
    Ef = 11.7
    Mu = get_ch_pot(Ef,t)
    bcs = 3.5/2.0
    delta0 = barmat.tools.get_delta0(tc, bcs=bcs)
    print delta0
    delta = deltaT(t, delta0, tc) 
    
    print delta0
    print delta

    Emin = 0.0  #eV
    Emax = 20.0 #eV


    freq = np.linspace(50E1,300E9,1000)
    hnu  = freq * (cs.h/cs.e)
        
    x  = np.linspace(Ef-20*delta,Ef+20*delta,step)
    I  = np.array([])
    I2 = np.array([])

    
    #for i in hnu:
        #integrale1 = Integrator("simps", x, MB_comp1, Ef-20*delta, Ef+20*delta, par= [i,t,Mu,delta] )
        #integrale1.run()
        #I=np.append(I,integrale1.integral)

        #x2 = np.linspace(delta-i, -delta, step)       
        
        #integrale2 = Integrator("quad", x2, MB_comp2, delta-i, -delta, par= [i,t,Ef,delta] )
        #integrale2.run()
        #I2 = np.append(I2,integrale2.integral)

        
    end = time()
    print "Execution time: "+str(end-start)


    for i in [0.00001,0.1,0.2,0.3,0.4,0.7,0.9,1.2,1.29,5000]:
        #plt.plot(x,MB_comp1(x,[ hnu[1], i, Ef, delta ]), label="T= "+str(i)+" K")
        delta = deltaT(t, delta0, tc)
        integrale1 = Integrator("quad", x, MB_comp2, delta-hnu[len(hnu)-1], -delta, par= [hnu[len(hnu)-1],t,Mu,delta] )
        integrale1.run()
        I=np.append(I,integrale1.integral)
        print integrale1.integral

    plt.plot([0.00001,0.1,0.2,0.3,0.4,0.7,0.9,1.2,1.29,5000], (2/hnu[1])*I)
    plt.legend(loc='best')
    plt.show()









