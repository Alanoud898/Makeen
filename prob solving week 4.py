x=[ 1,4,5,7,3,0]
for i in range(len(x)-1,0,-1):
    j= i-1
    if i>=j:
        print(x[i], end=" ")
    if max(x)== x[i]:
        break
print()
print("----------------")
y= [1,2,3,4]
for x in range(len(y)-1,0,-1):
    m= x-1
    if x>=m:
        print (y[x], end=" ")
    if max(y)== y[x]:
        break

