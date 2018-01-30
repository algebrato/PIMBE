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
    
    t = 1e3
    tc = 1.3
    Ef = 11.6
    bcs = 3.5/2.0
    delta0 = barmat.tools.get_delta0(tc, bcs=bcs)
    delta = deltaT(t, delta0, tc)

    Emin = 0.0  #eV
    Emax = 20.0 #eV


    freq = np.linspace(130E9,190E9,100)
    hnu  = freq * (cs.h/cs.e)
        
    x  = np.linspace(Ef-5*delta,Ef+5*delta,step)
    I  = np.array([])
    I2 = np.array([])

    for i in hnu:
        integrale2 = Integrator("quad",  x, MB_sempl, Ef-5*delta, Emax+5*delta, par= [i,t,Ef] )
        #integrale1 = Integrator("simps", x, MB_sempl, 0, 20, par= [i,t,Ef] ) #Non funziona...

        #integrale1.run()
        integrale2.run()


        #I = np.append(I,integrale1.integral)
        I2 = np.append(I2,integrale2.integral)
    
    end = time()
    print "Execution time: "+str(end-start)

    plt.plot(x,MB_sempl(x,[i,t,Ef]))
    plt.figure(2)
    plt.plot(hnu*(cs.e/cs.h), I2)
    plt.show()

    
