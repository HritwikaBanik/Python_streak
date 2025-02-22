
file_path = r"C:\Users\91600\Documents\GitHub\Algomagnet\Python_streak\CHAPTER 9\try_new.txt"
word = "DONKEY"

with open(file_path ,"r") as f:
    content = f.read()
    
    new= content.replace(word,"####")
with open(file_path ,"w") as f:
    f.write(new)