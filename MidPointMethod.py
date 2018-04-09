def f(x):
    return x*x + 2*x
def fdx(x):
    return 2*x + 2
#中点法,f为搜索的函数,fdx为f的导函数,interval 为搜索的区间
def MidPointMethod(fdx,interval):
    e = 10**-8
    a = float(interval[0])
    b = float(interval[1])

    while 1:
        lambda_ = (a + b)/2
        fdxl = fdx(lambda_)
        if abs(fdxl) < e:
            break
        elif fdxl > 0:
            # a = a
            b = lambda_
        else:
            a = lambda_
            #b = b
    return lambda_


if __name__ == "__main__":
    a = MidPointMethod(fdx,(-3,5))
    print(a)
