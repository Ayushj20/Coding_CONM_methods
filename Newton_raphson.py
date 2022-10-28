def f(x):
  return ((x*x)-x-1)
def f1(x1):
  return (2*x-1) 
a=float(input("Enter \"a\" value\n"))
b=float(input("Enter \"b\" value\n"))
e=float(input("Enter error\n"))
if(f(b)==0):
  print("Invalid intervals")
else:
  m=b-(f(b)/f1(b))
  i=1
try :
   while(f(abs(f(m)))<e):
     print(i,a,b,m,f(m))
     b=m
     m=b-(f(b)/f1(b))
     i=i+1
   print(i,a,b,m,f(m))
   print("Root are",m)
except:
  print("can\'t finding root" )
