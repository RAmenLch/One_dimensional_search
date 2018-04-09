def f(x):
    return 2*(x**4) - 4*(x**3) + 2*x*x + 3*x + 1
def fdx(x):
    return 8*(x**3) - 12*x*x + 4*x + 3
def fddx(x):
    return 24*x*x - 24*x

def f7(x):
    return x**3 - 2*x*x + x - 1
def f7dx(x):
    return 3*x*x - 2*x + 1

#牛顿法,fdx:f的导数,fddx:f的二阶导数,f为搜索的函数,ld为迭代的初值
#其实是求解方程 fdx(x) = 0 的解
def NewtonMethod(fdx,fddx,ld):
    e = 10**-6
    flag = True

    while 1:
        if abs(fdx(ld)) < e:
            break
        elif fddx(ld) <= 0:
            flag = False
            break
        else:
            ld1 = ld - fdx(ld)/fddx(ld)
            if abs(ld1 - ld) < e:
                break
            else:
                ld = ld1
    if flag :
        return ld
    else:
        raise ArithmeticError('此初值不收敛')

if __name__ == '__main__':
    ld = 5
    a = NewtonMethod(f7,f7dx,ld)
    print(a)
