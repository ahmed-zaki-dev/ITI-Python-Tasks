#    === To-Do List App ===


tasks_list = []

# Create Operation
def add_task():
    task = input("Please Fill your Task: ")
    tasks_list.append(task)
    print(f"Your Task [{task}] is added Successfully!\n")


# Read Operation
def read_task():
    if not tasks_list:
        print("No Tasks Found!\n")
        return
    print("These are your Tasks: ")

    for i, task in enumerate(tasks_list, start=1):
        print(f"{i}- {task}")
    print()


# Update Operation
def update_task():
    read_task()
    if not tasks_list:
        return

    index = int(input("Enter task number to update: ")) - 1
    if 0 <= index < len(tasks_list):
        new_task = input("Enter new task: ")
        tasks_list[index] = new_task
        print("Task updated successfully!\n")
    else:
        print("Invalid task number!\n")


# Delete Operation
def delete_task():
    read_task()
    if not tasks_list:
        return

    index = int(input("Enter task number to delete: ")) - 1
    if 0 <= index < len(tasks_list):
        removed = tasks_list.pop(index)
        print(f"Task [ {removed} ] deleted successfully!\n")
    else:
        print("Invalid task number!\n")


# Mark DONE Operation
def mark_done():
    read_task()
    if not tasks_list:
        return

    index = int(input("Enter task number to mark as Done: ")) - 1
    if 0 <= index < len(tasks_list):
        if not tasks_list[index].endswith("(Done)"):
            tasks_list[index] = tasks_list[index] + " (Done)"
            print("Task marked as Done!\n")
        else:
            print("Task is already Done!\n")
    else:
        print("Invalid task number!\n")


while True:
    print(" === To-Do List App === ")
    print(" 1--> Add Task" )
    print(" 2--> View Tasks ")
    print(" 3--> Update Task ")
    print(" 4--> Delete Task ")
    print(" 5--> Mark Task as Done")
    print(" 6--> Exit")

    choice = input("Choose an option (1-6): ").strip()

    if choice == "1":
        add_task()
    elif choice == "2":
        read_task()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        mark_done()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Try again.\n")