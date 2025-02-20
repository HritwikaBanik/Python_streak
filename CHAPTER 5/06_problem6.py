
s ={}

f1=input("Enter your name : ")
lang=input("Enter your fav language: ")
s.update({f1:lang})

f2=input("Enter your name : ")
lang=input("Enter your fav language: ")
s.update({f2:lang})

f3=input("Enter your name : ")
lang=input("Enter your fav language: ")
s.update({f3:lang})

f4=input("Enter your name : ")
lang=input("Enter your fav language: ")
s.update({f4:lang})

print(s)


'''if key is repeated : the latest value will be printed (or updated)
   if value is repeated : key will be printed twice '''