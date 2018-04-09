import numpy as np
def f(x):
    x1 = float(x[0,:])
    x2 = float(x[1,:])
    return 100*((x2-x1**2)**2) + (1-x1)**2
def deltaf(x):
    x1 = float(x[0,:])
    x2 = float(x[1,:])
    pdfdx1 = -400*x1*(-x1**2 + x2) + 2*x1 - 2
    pdfdx2 = -200*x1**2 + 200*x2
    return np.mat([pdfdx1,pdfdx2]).T
def GoldsteinMethod(f,deltaf,x,d,ld):
    rho = 1/10
    alpha = 3/2
    beta = 1/2
    xk = x
    dk = d
    ld = ld
    phi1 = f(xk)
    dPhi1 = deltaf(xk).T * dk
    while 1:
        phi2 = f(xk + ld * dk)
        if not phi2 <= phi1 + rho * dPhi1 * ld:
              ld = beta * ld
        elif not phi2 >= phi1 + (1-rho) * dPhi1 *ld:
             ld = alpha * ld
        else:
            break
    return ld
if __name__ == '__main__':
    x = np.mat([-1,1]).T
    d = np.mat([1,1]).T
    ld = GoldsteinMethod(f,deltaf,x,d,1)
    print(ld)
    print(x + ld *d)
    print(f(x + ld *d))
    #x = x + ld * d

    #d = np.mat([-1,0]).T

    #ld = GoldsteinMethod(f,deltaf,x,d)
    #print(f(x + ld *d))
