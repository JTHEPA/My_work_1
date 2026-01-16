import emoji

todo_list = []
print("To do list :}")
while True:   
    user_option = input("\nChoose an Option below \n\n1. View available Task\n2. Add Task\n3. Delete Task\n4. Exit\n\nOption : ")
    if user_option == '1':
        print(todo_list)
    elif user_option == '2':
        user_task = input("Enter Task : ")
        todo_list.append(user_task)
    elif user_option == '3':
        try:
            user_delete = input("Enter name of Task you would like to remove : ")
            if user_delete in todo_list:
                todo_list.remove(user_delete)
            else:
                print("Task not Available")
        except ValueError:
            print("Enter Valid name of Task")
    else:
        if user_option == '4':
            print(emoji.emojize("Bye :thumbs_up:"))
            quit()
        else:
            print("Enter Correct Option Next Time.")
            quit()
  
