import numpy as np
import scipy.constants as cs


def retta(x, par):
    return x

def rettapar(x,par):
    return par[0]*x+par[1]

def f_d(x,par):
    return 1/(np.exp((x-par[1])/((cs.k/cs.e)*par[0]))+1)

def MB_sempl(x,par):
    hnu = par[0]
    T   = par[1]
    Ef  = par[2]
    return ( (f_d(x,[T,Ef]) - f_d(x+hnu,[T,Ef])  ) *( np.power(x,2) + hnu*x) )/np.sqrt(( np.power(x,2) * np.power(x+hnu,2)))


def sigma1_MB_1th(x,par):
    #par[0] = w
    #par[1] = t
    #par[2] = Ef
    #par[3] = delta
    return (cs.e/(cs.hbar*par[0]))* (( fermi_dirac(x,[par[1],par[2]]) - fermi_dirac(x+(cs.hbar/cs.e)*par[0],[par[1], par[2]]  ) ) * ( x**2+par[3]**2+(cs.hbar/cs.e)*par[0]*x ))/(np.power( x**2-par[3]**2, 0.5 )*np.power((x+(cs.hbar/cs.e)*par[0])**2-par[3]**2,0.5 ))



def sigma1_MB_2th(x,par):
    #par[0] = w
    #par[1] = t
    #par[2] = Ef
    #par[3] = delta
    return (cs.e/(cs.hbar*par[0]))* (( 1 - 2*fermi_dirac(x+(cs.hbar/cs.e)*par[0],[par[1], par[2]]  ) ) * ( x**2+par[3]**2+(cs.hbar/cs.e)*par[0]*x ))/(np.power( x**2-par[3]**2, 0.5 )*np.power((x+(cs.hbar/cs.e)*par[0])**2-par[3]**2,0.5 ))

def deltaT(t, delta0, tc):
    return delta0*np.sqrt(1-np.power(t/tc,4))
