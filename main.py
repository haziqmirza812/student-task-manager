"""Console interface for the Student Task Manager."""

from task_manager import TaskManager

STORAGE_FILE = "tasks.json"

MENU = """
===== Student Task Manager =====
1. Add task
2. Display tasks
3. Complete task
4. Delete task
5. Exit
"""


def ask_task_id():
    """Ask for a task ID; return an int, or None if the input is not a number."""
    raw = input("Task ID: ").strip()
    if not raw.isdigit():
        print("Please enter a valid numeric task ID.")
        return None
    return int(raw)


def handle_add(manager):
    title = input("Task title: ")
    try:
        task = manager.add_task(title)
    except ValueError as error:
        print(f"Error: {error}")
        return
    print(f"Added: {task}")


def handle_display(manager):
    tasks = manager.list_tasks()
    if not tasks:
        print("No tasks yet.")
        return
    for task in tasks:
        print(task)


def handle_complete(manager):
    handle_display(manager)
    task_id = ask_task_id()
    if task_id is None:
        return
    try:
        task = manager.complete_task(task_id)
    except ValueError as error:
        print(f"Error: {error}")
        return
    print(f"Completed: {task}")


def handle_delete(manager):
    handle_display(manager)
    task_id = ask_task_id()
    if task_id is None:
        return
    task = manager.find_task(task_id)
    if task is None:
        print(f"Error: No task found with ID {task_id}.")
        return
    confirm = input(f"Delete '{task.title}'? (y/n): ").strip().lower()
    if confirm != "y":
        print("Delete cancelled.")
        return
    manager.delete_task(task_id)
    print(f"Deleted: {task}")


def main():
    manager = TaskManager(STORAGE_FILE)
    actions = {
        "1": handle_add,
        "2": handle_display,
        "3": handle_complete,
        "4": handle_delete,
    }
    while True:
        print(MENU)
        choice = input("Choose an option (1-5): ").strip()
        if choice == "5":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action is None:
            print("Invalid option, please choose 1-5.")
            continue
        action(manager)


if __name__ == "__main__":
    main()
