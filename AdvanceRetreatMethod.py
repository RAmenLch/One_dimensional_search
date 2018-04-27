import numpy as np

def AR(f):
    ld = -5
    dt = 1
    ld1 = ld + dt
    c = 0
    CMAX = 15
    if f(ld) < f(ld1):
        while c < CMAX:
            c += 1
            ld2=ld-2*dt
            if f(ld) < f(ld2):
                return (ld2,ld1)
            else:
                ld1 = ld
                ld = ld2
                dt = 2*dt
    else:
        while c < CMAX:
            c += 1
            ld2 = ld + 2*dt
            if f(ld1) <= f(ld2):
                return (ld,ld2)
            else:
                ld = ld1
                ld1 = ld2
                dt = 2*dt
    raise ValueError("进退法迭代%d次未找到极小值区间"%(CMAX))


if __name__ == "__main__":
    def f(x):
        return (x-50)**2
    print(AR(f))
