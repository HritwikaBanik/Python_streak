def check_manifest_in_poem():
    # Define the full file path (make sure to update it to the correct path where your file is located)
    file_path = r'C:\Users\91600\Documents\GitHub\Algomagnet\Python_streak\CHAPTER 9\poems.txt'
    
    # Open the file safely using 'with' to ensure it gets closed automatically
    with open(file_path, 'r') as f:
        content = f.read().strip()
        
    print("Content read from file:")
    print(repr(content))  # This will show any hidden characters (like \n or spaces)
    
    # Check if the word "manifest" is present in the content of the file
    if "Manifest" in content:
        print("manifest is present")
    else:
        print("manifest is NOT present")

# Call the function
check_manifest_in_poem()
