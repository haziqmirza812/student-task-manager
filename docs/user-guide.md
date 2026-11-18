# Student Task Manager – User Guide

This guide explains how to use the Student Task Manager from the command line.

## 1. Starting the program

Open a terminal in the project folder and run:

```bash
python main.py
```

The main menu appears:

```
===== Student Task Manager =====
1. Add task
2. Display tasks
3. Complete task
4. Delete task
5. Exit
```

Type the number of an option and press **Enter**.

## 2. Adding a task

1. Choose **1**.
2. Type the task title, for example `Submit DevOps lab`, and press Enter.
3. The program confirms: `Added: [ ] 1. Submit DevOps lab`.

An empty title (or one made only of spaces) is rejected with
`Error: Task title cannot be empty.` Titles longer than 100 characters are also rejected.

## 3. Displaying tasks

Choose **2**. Each task is listed with its ID:

```
[x] 1. Submit DevOps lab
[ ] 2. Revise for quiz
```

`[x]` means completed and `[ ]` means still pending.

## 4. Completing a task

1. Choose **3**. The current tasks are shown.
2. Enter the ID of the task you finished.
3. The task is marked `[x]`.

If the ID does not exist, or the task is already completed, an error message is shown
and nothing changes.

## 5. Deleting a task

1. Choose **4**. The current tasks are shown.
2. Enter the ID of the task to remove.
3. Confirm with `y` (any other answer cancels).

IDs are never reused, so after deleting task 2 the next new task still gets a new ID.

## 6. Exiting

Choose **5**. Your tasks are already saved in `tasks.json`, and they will be loaded
the next time you start the program.

## Troubleshooting

| Problem | Fix |
|---|---|
| `Invalid option, please choose 1-5.` | Type only the menu number. |
| `Please enter a valid numeric task ID.` | Enter digits only, such as `2`. |
| Want to start with an empty list | Delete the `tasks.json` file. |
