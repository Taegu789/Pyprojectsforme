import numpy as np

#가상의 기울기 a와 절편인 b를 정한다ㅡ
fake_a = 3
fake_b = 76

# 공부시간인 x 와 성적인 y의 배열을 만들어 줍니다.
x = np.array([2,4,6,8])
y = np.array([81,93,91,97])

# y= ax+b에 가상의 a,b의 값을 대입한 결과를 출력해주는 함수이다.

def predict(x):
    return fake_a*+fake_b

predicters = []

for i in range(len(x)) :
    predicters.append(predict(x[i]))
    print("공부시간 = %.f, 실제점수 = %.f, 예측점수 = %.f" % (x[i],y[i],predict(x[i])))

n = len(x)

def mse(y,y_pred) :
    return (1/n) * sum((y-y_pred)**2)

print("평균 제곱 오차 :"+ str(mse(y,predicters)))