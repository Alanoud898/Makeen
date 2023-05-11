word = str(input("write the word:"))
str=0
length=len(word)-1

while(word[str]<word[length]):
    ascii_code=ord(word[str])
    str=str+1
    print(ascii_code)