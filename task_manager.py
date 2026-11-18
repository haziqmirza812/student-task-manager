"""Core logic for the Student Task Manager."""

from dataclasses import dataclass


@dataclass
class Task:
    """A single task in the list."""

    id: int
    title: str
    completed: bool = False

    def __str__(self):
        mark = "x" if self.completed else " "
        return f"[{mark}] {self.id}. {self.title}"


class TaskManager:
    """Keeps the list of tasks and the operations on it."""

    def __init__(self):
        self.tasks = []
        self.next_id = 1

    # --- add feature ---
    def add_task(self, title):
        """Add a new task and return it."""
        task = Task(self.next_id, title)
        self.tasks.append(task)
        self.next_id += 1
        return task

    # --- display feature ---
    def list_tasks(self):
        """Return a copy of all tasks."""
        return list(self.tasks)

    def find_task(self, task_id):
        """Return the task with this ID, or None."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    # --- complete feature ---
    def complete_task(self, task_id):
        """Mark a task as completed (not implemented yet)."""
        raise NotImplementedError("Completing tasks is not available yet.")

    # --- delete feature ---
    def delete_task(self, task_id):
        """Delete a task (not implemented yet)."""
        raise NotImplementedError("Deleting tasks is not available yet.")
