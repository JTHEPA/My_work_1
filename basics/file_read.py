count = 0
try:
    with open("new.txt","r") as file:
        file_words = file.read()
        words = file_words.split()
        count += len(words)
except FileNotFoundError:
    print("file not found")
print(f"Number of words in file : {count}")

    
    
    