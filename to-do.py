tasks = []

def show_menu():
    print("\nTo-Do List")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")

def add_task():
    task = input("Enter your task to add: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks yet!")
    else:
        print("Your Tasks to Do:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def delete_task():
    if len(tasks) == 0:
        print("No task to delete!")
    else:
        view_tasks()
        d = int(input("Enter your task number to delete: "))
        if 1 <= d <= len(tasks):
            removed = tasks.pop(d - 1)
            print(f"Task '{removed}' deleted successfully!")
        else:
            print("Invalid task number!")

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    print("Tasks saved!")

# Main loop
while True:
    show_menu()
    yr_choice = input("Enter Your Choice of Task: ")

    if yr_choice == "1":
        add_task()
    elif yr_choice == "2":
        view_tasks()
    elif yr_choice == "3":
        delete_task()
    elif yr_choice == "4":
        save_tasks()
        print("Goodbye!")
        break
    else:
        print("Invalid Choice!")