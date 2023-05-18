file=open("problem.txt","r")
employee={}
salary=[]
for line in file:
    data=line.split()
    salary.append(float(data[0]))
    employee[data[1]]=data[0]
print(employee)
print(salary)
avg=sum(salary)/len(salary)
print(avg)
x=max(salary)
for key in employee:
    if(float(employee[key]) ==x):
        print (key)
       