x=[[1,1,1],
   [2,2,2],
   [3,3,3]]
for i in range(3):
    for j in range(3):
        print(x[i][j],end=" ")
    print()


a=[[i]*3 for i in range(4) if i>0]
print(a)