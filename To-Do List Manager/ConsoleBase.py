import os
import json

# ------------------------- File Handling ------------------------------
File_Name = "tasks.json"

# Loading tasks
def load_tasks():
    if os.path.exists(File_Name):
        with open(File_Name, "r") as file:
            return json.load(file)
    return []

# Saving tasks
def save_tasks(tasks):
    with open(File_Name, "w") as file:
          json.dump(tasks, file, indent=4)

# ------------------------- File Handling ------------------------------


# ---------------------------- Task Functions ------------------------------

# Show tasks
def show_tasks(tasks):
    if tasks:
        print(f"\nTo-Do List")
        for i, task in enumerate(tasks, start=1):
            status = '✓' if task['Completed'] else '✗'
            print(f"{i}. {task['Task']} [{status}]")
        print()
    else:
        print("\nNo Tasks found\n")
        return

# Add task
def add_task(tasks):
    task_name = input("Enter new Task: ")
    for task in tasks:
        if task['Task'] == task_name:
            print("\nTask already exists\n")
            return
    else:
        if task_name:
            tasks.append({"Task" : task_name , "Completed" : False})
            print(f"\nTask '{task_name}' added to your To-Do List\n")
        else:
            print("\nTask cannot be empty\n")

# Remove tasks
def remove_task(tasks):
    show_tasks(tasks)
    if not tasks:
        print("\nNo Tasks found\n")
        return
    try:
      task_index = int(input("\nEnter number of task to remove: "))
      task_index_modified = task_index - 1
      if 0 <= task_index_modified < len(tasks):
         removed = tasks.pop(task_index_modified)
         print(f"\nTask '{removed['Task']}' removed\n")
      else:
         print(f"\nNo task found with number {task_index}\n")
    except ValueError:
         print("\nInvalid number\n")

# Marked tasks complete
def marked_tasks(tasks):
    show_tasks(tasks)
    if not tasks:
        print("\nNo Tasks found\n")
        return
    try:
        task_index = int(input("\nEnter number of task to mark: "))
        task_index_modified = task_index - 1
        if 0 <= task_index_modified < len(tasks):
            tasks[task_index_modified]['Completed'] = True
            print(f"\nTask '{tasks[task_index_modified]['Task']}' is marked as Completed\n")
        else:
            print(f"\nNo task found with number {task_index}\n")
    except ValueError:
        print("\nInvalid number\n")

# ---------------------------- Task Functions ------------------------------


# ------------------------- ConsoleBase-UI ----------------------------

def main():
    tasks = load_tasks()
    while True:
        print("-------- To-Do List Manager --------")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Mark Task Complete")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            marked_tasks(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("\nTasks saved! Bye.\n")
            break
        else:
            print("\nInvalid choice\n")

if __name__ == "__main__":
    main()

# ------------------------- ConsoleBase-UI ----------------------------
