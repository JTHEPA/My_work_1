count = 0
with open("new.txt","r") as file:
    file_words = file.read()
    words = file_words.split()
    count += len(words)
    
print(f"Number of words in file : {count}")
    
    
    