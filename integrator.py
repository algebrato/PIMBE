from threading import Thread
from scipy.integrate import quad
from scipy.integrate import simps
from funct import *
import numpy as np


class Integrator(Thread):
    #Costruttore
    def __init__(self, method, x, funz, xlim_inf=None, xlim_sup=None, par=None):
        Thread.__init__(self)
        self.method     = method
        self.x          = x
        self.y          = funz(x,par)
        self.function   = funz
        self.xlim_inf   = xlim_inf
        self.xlim_sup   = xlim_sup
        self.par        = par
        self.integral   = 0


    def integrate(self):
        if self.method == "simps":
            self.integral = simps(self.y,self.x)
        elif self.method == "quad":
            self.integral = quad(self.function, self.xlim_inf, self.xlim_sup, args=self.par )[0]
        else:
            print("Error! Unknow Integrator Type")
     
            return -1

    def run(self):
        self.integrate()







