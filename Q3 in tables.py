n=[[0]*5 for i in range(5)]
for i in range(4):
    for j in range(4):
        if (i+j)%2==0:
            n[i][j]=1
for i in range(4):
    for j in range(4):
      print(n[i][j],end=" ")
    print()