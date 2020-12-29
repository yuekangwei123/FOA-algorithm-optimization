# 该方法可以运行,适用于只调一个参数的方法
import numpy as np
import matplotlib.pyplot as plt
#定义需要解的函数(名称为fun1)
def fun1(arr):
    y = 2*arr**2-1
    return y
#######果蝇算法######
##初始化果蝇参数
popsize = 30  #果蝇种群规模
maxgen = 100  #果蝇最大迭代次数
R = 1        #果蝇飞行半径
D = 1        #优化变量个数
X = np.zeros([popsize,D])
Dist = np.zeros([popsize,D])
S = np.zeros([popsize,D])
Smell = np.zeros([popsize,1])
X = np.zeros([popsize,D])
Y = np.zeros([popsize,D])
fitness = np.zeros([maxgen,1])
#赋予果蝇群体初始位置
X_axis = np.random.rand(1,D)
print(X_axis)
Y_axis = np.random.rand(1,D)
#赋予果蝇种群飞行半径
for i in range(popsize):
    X[i,:] = X_axis + R*(2*np.random.rand(1,D)-1)
    Y[i,:] = Y_axis + R*(2*np.random.rand(1,D)-1)
    #计算距离Dist
    Dist[i,:] = np.sqrt(X[i,:]**2+Y[i,:]**2)
    #计算味道浓度的倒数作为味道浓度判定值
    S[i,:] = 1/Dist[i,:]
    #带入味道浓度函数中求出味道浓度值
    Smell[i] = fun1(S[i,:])
#找出味道浓度最大值
Smellbest,index = np.min(Smell),np.argmin(Smell)
bestSmell = Smellbest
#保留最佳味道浓度处的果蝇
X_axis = X[int(index),:]
Y_axis = Y[int(index),:]
#果蝇种群进入迭代寻优
for j in range(maxgen):
    for i in range(popsize):
        X[i,:] = X_axis + R*(-20*np.random.rand(1,D)-1)
        Y[i,:] = Y_axis + R*(-20*np.random.rand(1,D)-1)
        #计算距离Dist
        Dist[i,:] = np.sqrt(X[i,:]**2+Y[i,:]**2)
        #计算味道浓度的倒数作为味道浓度判定值
        S[i,:] = 1/Dist[i,:]
        #带入味道浓度函数中求出味道浓度值
        Smell[i] = fun1(S[i,:])
    Smellbest,index = np.min(Smell),np.argmin(Smell)
    if Smellbest < bestSmell:
        bestSmell = Smellbest
        X_axis = X[int(index),:]
        Y_axis = Y[int(index),:]
    fitness[j] = bestSmell
plt.figure(1)
plt.plot(range(maxgen),fitness)
plt.show()
plt.xlabel('迭代次数')
plt.ylabel('味道浓度值')
