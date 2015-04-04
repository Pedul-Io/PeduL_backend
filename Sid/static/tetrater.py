from cmath import *
from sympy import *


def apx(arg,bou):
    if bou == 1:
        return arg
    return arg**(apx(arg,bou-1))
def trueterm(arg,bou):
    return apx(arg,bou)/factorial(bou)

i= 1
while(i < 100):
    print trueterm(2,i)
    i+=1
