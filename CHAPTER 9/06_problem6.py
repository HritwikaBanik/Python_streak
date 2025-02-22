file_path = r"C:\Users\91600\Documents\GitHub\Algomagnet\Python_streak\CHAPTER 9\log.html"

with open(file_path , "r") as f:
    content = f.read()
    if "python" in content :
        print("Found")
    else:
        print("Not found")