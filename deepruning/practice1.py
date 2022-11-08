import numpy as np

w11 = np.array([-2, -2])
w12 = np.array([2,2])
w2 = np.array([1,1])
b1 = 3
b2 = -1
b3 = -1
# MLP 함수는 퍼셉트론 함수이다. 0,1 중에서 하나를 출력하게 해준다.
def MLP(x,w,b):
    y = np.sum(w*x) + b
    if y <=0 :
        return 0
    else:
        return 1
    
#NAND 게이트
def NAND(x1,x2) :
    return MLP(np.array([x1,x2]),w11,b1)
