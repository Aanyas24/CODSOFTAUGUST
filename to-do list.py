import json
import os

def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("No tasks.")
    else:
        print("Tasks:")
        for idx, task in enumerate(tasks, start=1):
            status = "✓" if task["completed"] else " "
            print(f"{idx}. [{status}] {task['description']}")

def add_task(tasks, description):
    tasks.append({"description": description, "completed": False})
    save_tasks(tasks)
    print("Task added.")

def complete_task(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed.")
    else:
        print("Invalid task index.")

def main():
    tasks = load_tasks()

    while True:
        print("\n1. Show Tasks\n2. Add Task\n3. Complete Task\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            description = input("Enter task description: ")
            add_task(tasks, description)
        elif choice == "3":
            show_tasks(tasks)
            task_index = int(input("Enter task index to mark as completed: "))
            complete_task(tasks, task_index)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")
            

if __name__ == "__main__":
    main()
    
