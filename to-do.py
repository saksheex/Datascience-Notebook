
def show_menu():
    print("To-Do List")
    print("1. Add task")
    print("2. View Task")
    print("3. Delete Task")
    print("4. Quit")  
tasks = []
yr_choice= input('Enter Your Choice of Task: ')
if yr_choice=="1":
        print("you are into task add")
elif yr_choice == "2":
        print("you are into task view")
elif yr_choice == "3":
        print("you are into task delete")
elif yr_choice == "4":
        print(" Quitting, Goodbye")
       
else:
        print("Invalid Choice")
def add_task():
    task = input("Enter your task to add : ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")
    add_task()
def view_tasks():
     if yr_choice == "2":
         view_tasks() 
     elif len(tasks) == 0:
        print("No tasks yet!")
     else:
        print("Your Tasks to Do")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")   
        view_tasks()
def delete_task():
        if yr_choice == "3":
           delete_task() 
        elif len(tasks) == 0:
            print("No task to Delete")
        else:
            d= int(input("Enter your task numebr to delete"))
            removed= tasks.pop(d-1)
            print(f"Task {removed} deleted successfully")
            delete_task()
def save_tasks():
        if yr_choice == "4":
           save_tasks()
           print("Goodbye!")
        else:
             with open("tasks.txt", "w") as file:
              for task in tasks:
               file.write(task + "\n")
              print("Tasks saved!")  
              save_tasks()  
# def make_lower(a):
#     if any(char.isupper() for char in a):
#         print("Capital letter found, converting to lowercase")
#         return a.lower()
#     else:
#         print("You are good to go, no capitals found!")
#         return a

# text = input("Enter your inputs: ")
# result = make_lower(text)
# print("Final Version after review:", result)  
show_menu()