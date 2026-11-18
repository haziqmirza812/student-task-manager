"""Core logic for the Student Task Manager."""

import json
import os
from dataclasses import asdict, dataclass

MAX_TITLE_LENGTH = 100


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

    def __init__(self, storage_file=None):
        self.storage_file = storage_file
        self.tasks = []
        self.next_id = 1
        if self.storage_file:
            self.load()

    # --- storage ---
    def load(self):
        """Load tasks from the JSON storage file, if it exists."""
        if not self.storage_file or not os.path.exists(self.storage_file):
            return
        with open(self.storage_file, encoding="utf-8") as f:
            data = json.load(f)
        self.tasks = [Task(**item) for item in data.get("tasks", [])]
        self.next_id = data.get("next_id", len(self.tasks) + 1)

    def save(self):
        """Write all tasks to the JSON storage file."""
        if not self.storage_file:
            return
        data = {"next_id": self.next_id, "tasks": [asdict(t) for t in self.tasks]}
        with open(self.storage_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    # --- add feature ---
    def add_task(self, title):
        """Add a new task and return it.

        Raises ValueError if the title is empty or only whitespace.
        """
        if title is None or not str(title).strip():
            raise ValueError("Task title cannot be empty.")
        title = str(title).strip()
        if len(title) > MAX_TITLE_LENGTH:
            raise ValueError(f"Task title cannot exceed {MAX_TITLE_LENGTH} characters.")
        task = Task(self.next_id, title)
        self.tasks.append(task)
        self.next_id += 1
        self.save()
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
