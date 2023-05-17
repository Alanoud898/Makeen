"""x=[]
a=int(input("Enter num:"))
for i in range(0,a):
    b=int(input())
    x.append(b)
print(x)"""



n=[[0]*5 for i in range(5)]
for i in range(4):
    for j in range(4):
        if [i]==[j]:
            n[i][j]=1
        elif[i]>[j]:
            n[i][j]=2
for i in range(4):
    for j in range(4):
      print(n[i][j],end=" ")
    print()
            
            
                
            
    
            
