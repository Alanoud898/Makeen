total=0.0
count=0
num=int(input("enter num of vlue"))
for i in range (num):
    inputStr = int(input("Enter value: "))
    total = total + inputStr
    count+=1
    #print(total)
   # inputStr = input("Enter value: ")
if count > 0 :
    average = total / count
else :
    average = 0.0
print(average)