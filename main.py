def load_tasks():
    try:
        with open("tasks.txt", "r", encoding="utf-8") as f:
            tasks = []
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split("|", 1)
                    if len(parts) == 2:
                        done = parts[0] == "1"
                        task_text = parts[1]
                        tasks.append({"task": task_text, "done": done})
            return tasks
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open("tasks.txt", "w", encoding="utf-8") as f:
        for task in tasks:
            done_flag = "1" if task["done"] else "0"
            f.write(f"{done_flag}|{task['task']}\n")


def show_tasks(tasks):
    print("\n=== TODO LIST ===")
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, start=1):
            mark = "[x]" if task["done"] else "[ ]"
            print(f"{i}. {mark} {task['task']}")
    print()


def add_task(tasks):
    task_text = input("Enter a new task: ").strip()
    if task_text:
        tasks.append({"task": task_text, "done": False})
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
        print(f"Deleted: {removed['task']}\n")
    else:
        print("Task number out of range.\n")


def mark_task_done(tasks):
    show_tasks(tasks)
    if not tasks:
        return

    choice = input("Enter the task number to mark as done: ").strip()
    if not choice.isdigit():
        print("Please enter a valid number.\n")
        return

    index = int(choice) - 1
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
        print(f"Marked as done: {tasks[index]['task']}\n")
    else:
        print("Task number out of range.\n")


def main():
    tasks = load_tasks()

    while True:
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Mark task as done")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_task_done(tasks)
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()