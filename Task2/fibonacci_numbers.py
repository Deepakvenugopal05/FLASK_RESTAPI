def fibo(n):
    if (n<=1):
        return n
    elif(n==2):
        return 1
    return fibo(n-1)+fibo(n-2)

n = int(input('Enter n.o:'))
for i in range(n): 
    print(fibo(i),end=' ')
