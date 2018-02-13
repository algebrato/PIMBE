import numpy as np
import scipy.constants as cs


def retta(x, par):
    return x

def rettapar(x,par):
    return par[0]*x+par[1]

def f_d(x,par):
    return 1/(np.exp((x-par[1])/((cs.k/cs.e)*par[0]))+1)

def MB_sempl(x,par): #Ok questa sembra che venga integrata in modo corretto con simps
    hnu = par[0]
    T   = par[1]
    Ef  = par[2]
    return ( (f_d(x,[T,Ef]) - f_d(x+hnu,[T,Ef])  ) *( np.power(x,2) + hnu*x) )/np.sqrt(( np.power(x,2) * np.power(x+hnu,2)))

def MB_comp1(x,par):
    hnu   = par[0]
    T     = par[1]
    Ef    = par[2]
    delta = par[3]
    return ( (  f_d(x,[T,Ef]) - f_d(x+hnu,[T,Ef])  ) *( np.power(x,2) + np.power(delta,2) + hnu*x) )/(np.sqrt(( np.power(x,2) - np.power(delta,2) )) * np.sqrt( ( np.power(x+hnu,2) -np.power(delta,2) )))

def MB_comp2(x,par):
    hnu   = par[0]
    T     = par[1]
    Ef    = par[2]
    delta = par[3]
    return ( (  1 - 2*f_d(x+hnu,[T,Ef])  ) *( np.power(x,2) + np.power(delta,2) + hnu*x) )/(np.sqrt(( np.power(x,2) - np.power(delta,2) )) * np.sqrt( ( np.power(x+hnu,2) -np.power(delta,2) )))


def MB_comp1_bis(x,par):
    hnu   = par[0]
    T     = par[1]
    Ef    = par[2]
    delta = par[3]

    return ( ( np.power(x,2) + np.power(delta,2) + hnu*x) )/(np.sqrt(( np.power(x,2) - np.power(delta,2) )) * np.sqrt( ( np.power(x+hnu,2) -np.power(delta,2) )))


# definition given by MUHLSCHLEGHEL


def get_ch_pot(Ef,t):
    return Ef*(1-(1/3)*(cs.pi*cs.k*t/cs.e)/(2*Ef))


def deltaT(t, delta0, tc):
    return delta0*np.sqrt( np.cos((np.pi/2)*(t/tc)) ) 

def test_func(x,par):
    T   = par[0]
    Ef  = par[1]
    hnu = par[2]
    return (f_d(x,[T,Ef]) - f_d(x+hnu,[T,Ef]))



