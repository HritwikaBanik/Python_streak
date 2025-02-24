#list

l =["Tina " ,"Mina","Rina","na"]
n = []

def remove(l,word):
    for item in l:
        if not(item == word):
           n.append(item.strip(word))
    return n



print("After removing the word :" ,remove(l,"na"))
    