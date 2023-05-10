size=int(input("Enter the fils size:"))
files=int(input("Enter the num of files:"))
size_of_one_file=int(input("Enter the size of one file:"))
total_size= files*size_of_one_file
if total_size<=size:
         print("yes")
else:
         print("no")