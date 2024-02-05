print("start with a new day")
n=int(input())
k=n-1
for i in range(0,n):
    for j in range(0,k):
        print(end=" ")
        
    k=k-1
    for j in range(0,i+1):
        print('*',end=" ")
    print("\r")
    
n1=65 
for i in range(0,n):
    for j in range(1,i+1):
        ch=chr(n1)
        print(ch,end=" ")
        n1=n1+1
    print('\r')