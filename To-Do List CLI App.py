def todo_app():
    todo_list = []
    
    while True:
        print("\n--- TO-DO LIST ---")
        print("1. View Tasks\n2. Add Task\n3. Delete Task\n4. Exit")
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            if not todo_list:
                print("Your list is empty!")
            for index, task in enumerate(todo_list, 1):
                print(f"{index}. {task}")
        elif choice == "2":
            task = input("Enter the task: ")
            todo_list.append(task)
            print(f"'{task}' added!")
        elif choice == "3":
            if todo_list:
                task_num = int(input("Enter task number to delete: "))
                if 0 < task_num <= len(todo_list):
                    removed = todo_list.pop(task_num - 1)
                    print(f"Removed: '{removed}'")
                else:
                    print("Invalid task number.")
            else:
                print("Nothing to delete.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

todo_app()