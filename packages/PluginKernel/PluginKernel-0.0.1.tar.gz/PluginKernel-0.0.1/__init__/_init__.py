import numpy as np
def kernelplugin(X):
    msup = max(X)
    minf = min(X)
    l = (msup - minf) / 2
    mini = minf - l
    maxi = msup + l
    r = (maxi - mini) / 100
    n = len(X)
    P = 100
    P0 = 2000
    e = -100
    d = 100
    c = (2 * np.pi)**0.5
    I = 0
    for k in range(1, P0+1):
        zk = e + (d-e) * k/P0
        u = np.exp(-(zk**4)/4)
        I += u
    MK = I * (d-e) / (c*c*P0)
    Jf = 1
    

    for NBI in range(1,10):
        #Estimation de hN
        hn = (MK**0.2) * (Jf*n)**(-0.2)
        valeur=2*2.23*(hn)**(-6)/500
        Y = []
        Yk = []
        for k in range(P):
            yk = mini + (maxi-mini)*k/P
            Y.append(0)
            Yk.append(yk)
            for i in range(1,n):
                z = (yk-X[i]) / hn
                z = z**2
                z = -0.5*z
                z = np.exp(z)
                Y[-1] += z
            Y[-1] = Y[-1] / (c*n*hn)
        e = -100
        d = 100
        I = 0
        Jf = 0
        z = 0
        for k in range(1, P-2):
            z = (Y[k+1]-2*Y[k]+Y[k-1])
            I += z**2
        I = I + ((Y[P-2])**2 + (Y[P-2]-2*Y[P-3])**2) / (r**4)
        #Estimation de Jf 
        Jf = I / (r**3)
        
    return Y
