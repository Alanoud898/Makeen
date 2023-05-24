""""c_to_f= lambda x:(x*9/5)+32
print(c_to_f(30))"""


"""mult= lambda x, y: x * y
result = mult(5, 3)
print(result)"""  

"""add=lambda*args:sum(arges)
print(add(20,3,40,5))"""

"""list=[{"name":"John","age":28},
{"name":"Mary","age":23},
{"name":"Bob","age":35},
{"name":"Alic","age":32}]
sorted_list = sorted(list, key=lambda x: x['age'])
print(sorted_list)"""


"""people=[{"name":"John","age":28},
{"name":"Mary","age":23},
{"name":"Bob","age":35},
{"name":"Alic","age":32}]
sorted_list= sorted(people, key= lambda x:x["age"])
print(sorted_list)"""

"""nums=[-4,6,8,-1,3,-5]
new_list= list(filter(lambda x: x >=0, nums))
print(new_list)"""

#filter

"""list1=["Alanoud","FATMA","Ali","sara"]
lowercase= list(filter(lambda x: x.islower(), list1))
uppercase= list(filter(lambda x: x.isupper(), list1))
print(lowercase)
print(uppercase)"""

#map

"""list1 = ["alanoud", "fatma", "ali", "sara"]
uppercase= list(map(lambda x: x.upper(), list1))
print(uppercase)"""

#Reduce

"""from functools import reduce
nums= [1, 2, 3, 4, 5]
sum_of_squares= reduce(lambda x, y: x + y**2, nums, 0)
print(sum_of_squares)"""  











