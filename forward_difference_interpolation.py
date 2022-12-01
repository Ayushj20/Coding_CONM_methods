import numpy as np
def fact(n):
    f = 1;
    for i in range(2, n + 1):
        f *= i;
    return f;
def cal(u,n):
  t=u
  for i in range(1,n):
    t = t * (u - i);
  return(t)
n = int(input('Enter number of data points: '))
x = np.zeros((n))
y = np.zeros(n)
d=np.zeros((n,n))
for i in range(n):
    x[i] = float(input('x='))
    y[i]= float(input('y='))
for j in range(1,n):
    for i in range(0,n-j):
      if j==1:
        d[i][j]=y[i+1]-y[i]
      else:
        d[i][j] = d[i+1][j-1] - d[i][j-1]
for i in range(0,n):
    for j in range(1, n-i):
        print('\t\t%0.2f' %(d[i][j]), end='')
    print()
v=int(input("enter the value to calculate:\n"))
h=x[1]-x[0]
u=(v-x[0])/h
sum=y[0]
for i in range(n):
  sum+=(cal(u,i)*d[0][i])/fact(i)
print("the value of y at x=",v,"is",sum)