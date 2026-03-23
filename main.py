def load_tasks():
    try:
        with open("tasks.txt", "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(task + "\n")

def show_tasks(tasks):
    print("\n=== TODO LIST ===")
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    print()

def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added.\n")
    else:
        print("Task cannot be empty.\n")

def delete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    choice = input("Enter the task number to delete: ").strip()
    if not choice.isdigit():
        print("Please enter a valid number.\n")
        return
    index = int(choice) - 1
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Deleted: {removed}\n")
    else:
        print("Task number out of range.\n")

def main():
    tasks = load_tasks()

    while True:
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    main()