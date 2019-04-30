import numpy as np

T = 0.5        #时间半年
N = input ('Please input the steps：')  
N = int (N)      #输入N
C = input ('Please input 1 or 0,0 for Call option 1 for Put option：')  
C = int (C)      #输入N
CP = (-1)**(C-1) #确定是否看涨还是看跌期权
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
    return max((strike-spot)*CP,0) #定义函数计算在到期日期权价值

for i in range(N,0,-1):
    for j in range (i,0,-1):
        if i == N:  #在到期日计算到期日前一个时间周期
            lattice[i-1][j-1] = max(discount * (p*(poo(lattice[i,j]))+(1-p)*(poo(lattice[i][j-1]))), CP*(strike-lattice[i-1][j-1]))
        else:
            lattice[i-1][j-1] = max(discount * (p*lattice[i, j] + (1-p)*lattice[i][j - 1]),CP*(strike-(lattice[i-1][j-1])))  #非到期日计算
onetimes = lattice[0][0]
print ("The price of the option is:")
print (onetimes)

#以下为验证公式C0(aS0,aK)/C0(S0,k)=a

a = input ('a times strike and spot:')  
a = int (a)  
strike = a*50    #敲定价格
spot = a*48      #当前价格

lattice = np.zeros((N+1, N+1))     #生成矩阵

lattice[0][0] = spot               #定义左上角

for i in range(N):
    for j in range(i+1):
     lattice[i+1][j+1] = up * lattice[i][j]
     lattice[i+1][0] = down * lattice[i][0] #价格矩阵

def poo(spot):
    return max((strike-spot)*CP,0) #定义函数计算在到期日期权价值

for i in range(N,0,-1):
    for j in range (i,0,-1):
        if i == N:  #在到期日计算到期日前一个时间周期
            lattice[i-1][j-1] = max(discount * (p*(poo(lattice[i,j]))+(1-p)*(poo(lattice[i][j-1]))), CP*(strike-lattice[i-1][j-1]))
        else:
            lattice[i-1][j-1] = max(discount * (p*lattice[i, j] + (1-p)*lattice[i][j - 1]),CP*(strike-(lattice[i-1][j-1]))) 
atimes = lattice[0][0]
print ("C0(aS0,aK)/C0(S0,k)=")
print (atimes/onetimes)
