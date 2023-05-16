password=input("Enter your password:")
l,u,p,d=0,0,0,0
if (len(password)>=8):
    for i in password:
        if(i.islower):
           l+=1
        if(i.isupper()):
           u+=1
        if(i.isdigit()):
           d+=1
        if(i=='@' or i=='$' or i=='#'):
            p+=1
if (1>=1 and u>=1 and p>=1 and d>=1 and 1+p+u+d==len(password)):
    print("valid")
else:
    print("invalid")
            
            

         
         
  

    
    
    
        
    
        

            
            
