import numpy as np

T = 0.5        #时间半年
N = input ('Please input the steps：')  
N = int (N)      #输入N
r = 0.03       #无风险利率
sigma = 0.3    #波动率
strike = 50    #敲定价格
spot = 48      #当前价格

dt = T / N  
up = np.exp(sigma*np.sqrt(dt))     #u
down = 1/up                        #d
p=((np.exp(r*dt)-down)/(up-down))  #股价上涨概率
discount = np.exp(-r*dt)           #贴现

lattice = np.zeros((N+1, N+1))     #生成矩阵

lattice[0][0] = spot               #定义左上角

for i in range(N):
    for j in range(i+1):
     lattice[i+1][j+1] = up * lattice[i][j]
     lattice[i+1][0] = down * lattice[i][0] #价格矩阵

def poo(spot):
    return max(50-spot,0) #定义函数计算在到期日期权价值

for i in range(N,0,-1):
    for j in range (i,0,-1):
        if i == N:  #在到期日计算到期日前一个时间周期
            lattice[i-1][j-1] = discount * (p*(poo(lattice[i,j]))+(1-p)*(poo(lattice[i][j-1])))
        else:
            lattice[i-1][j-1] = discount * (p*lattice[i, j] + (1-p)*lattice[i][j - 1])  #非到期日计算

print (lattice[0][0])
