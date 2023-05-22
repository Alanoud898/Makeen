class Stack:
    def __init__(self,items):
        self.items =items

    
         
    def push(self,item):
       self.items.append(item)
    
   
    def find_pop(self,r):
        for i in range(len(self.items)):
            r.append(self.items.pop())
        return r
item= Stack([])
item.push("H")
item.push("e")
item.push("l")
item.push("l")
item.push("o")
print(item.find_pop([]))