#黄金分割法,f为搜索的函数,interval 为搜索的区间
def GSM(f,interval):
    GAMMA = (5**0.5-1)/2
    e = 10**-8
    alpha = float(interval[0])
    beta = float(interval[1])

    lambdak = (beta - alpha)*(1-GAMMA) + alpha
    muk = (beta - alpha)*(GAMMA) + alpha
    PhiLambdak = f(lambdak)
    PhiMuk = f(muk)

    while( beta - alpha >= e ):
        di = PhiLambdak - PhiMuk
        if di == 0:
            alpha = lambdak
            beta = muk
            lambdak = (beta - alpha)*(1-GAMMA) + alpha
            muk = (beta - alpha)*(GAMMA) + alpha
            PhiLambdak = f(lambdak)
            PhiMuk = f(muk)
        elif di < 0:
            #alpha = alpha
            beta = muk
            muk = lambdak
            lambdak = (1-GAMMA)*(beta - alpha) + alpha
            PhiMuk = PhiLambdak
            PhiLambdak = f(lambdak)
        else:
            alpha = lambdak
            #beta = beta
            lambdak = muk
            muk = (beta - alpha)*(GAMMA) + alpha
            PhiLambdak = PhiMuk
            PhiMuk = f(muk)

    return (beta + alpha)/2



if __name__ == '__main__':
    def f(x):
        return x*x + 2*x
    a = GSM(f,(-3,5))
    print(a)
