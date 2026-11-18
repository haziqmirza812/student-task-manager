"""Unit tests for the Student Task Manager."""

import os
import tempfile
import unittest

from task_manager import TaskManager


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        task = self.manager.add_task("Finish DevOps lab")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Finish DevOps lab")
        self.assertFalse(task.completed)
        self.assertEqual(len(self.manager.list_tasks()), 1)

    def test_add_task_rejects_empty_title(self):
        with self.assertRaises(ValueError):
            self.manager.add_task("")
        with self.assertRaises(ValueError):
            self.manager.add_task("   ")
        self.assertEqual(self.manager.list_tasks(), [])

    def test_complete_task(self):
        task = self.manager.add_task("Read chapter 4")
        self.manager.complete_task(task.id)
        self.assertTrue(self.manager.find_task(task.id).completed)

    def test_complete_task_twice_raises_error(self):
        task = self.manager.add_task("Read chapter 4")
        self.manager.complete_task(task.id)
        with self.assertRaises(ValueError):
            self.manager.complete_task(task.id)

    def test_delete_task(self):
        first = self.manager.add_task("Task one")
        self.manager.add_task("Task two")
        self.manager.delete_task(first.id)
        remaining = self.manager.list_tasks()
        self.assertEqual(len(remaining), 1)
        self.assertIsNone(self.manager.find_task(first.id))

    def test_delete_task_with_invalid_id(self):
        self.manager.add_task("Task one")
        with self.assertRaises(ValueError):
            self.manager.delete_task(99)
        with self.assertRaises(ValueError):
            self.manager.delete_task(0)
        self.assertEqual(len(self.manager.list_tasks()), 1)

    def test_tasks_are_saved_and_loaded(self):
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "tasks.json")
            saver = TaskManager(path)
            saver.add_task("Persisted task")
            loader = TaskManager(path)
            self.assertEqual(loader.list_tasks()[0].title, "Persisted task")
            self.assertEqual(loader.next_id, 2)


if __name__ == "__main__":
    unittest.main()
