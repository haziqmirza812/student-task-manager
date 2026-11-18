# Student Task Manager

A small Python console application for students to keep track of their tasks.
It was built for Lab Assignment 4 of **CSC418 – DevOps for Cloud Computing** to practise
a complete Git and GitHub workflow: commits, branches, Issues, Pull Requests, merge
conflicts, GitHub Actions and releases.

![Python tests](https://github.com/haziqmirza812/student-task-manager/actions/workflows/tests.yml/badge.svg)

Project status: In Progress - testing underway

## Features

- **Add tasks** – empty or whitespace-only titles are rejected, titles are limited to 100 characters.
- **Display tasks** – every task is shown with its ID and a `[ ]` / `[x]` completion box.
- **Complete tasks** – mark a selected task as completed by its ID; completing it twice is reported.
- **Delete tasks** – delete a task using a valid task ID, with a confirmation prompt.
- **Saved between runs** – tasks are stored in `tasks.json` in the project folder.
- **Automated tests** – `unittest` suite run by GitHub Actions on every push and Pull Request to `main`.

## Project structure

```
student-task-manager/
├── main.py                  # console menu (user interface)
├── task_manager.py          # Task and TaskManager classes (core logic + JSON storage)
├── tests/
│   └── test_task_manager.py # unittest test suite
├── docs/
│   └── user-guide.md        # short user guide
├── lab-evidence/            # screenshots of key assignment steps
├── .github/workflows/
│   └── tests.yml            # GitHub Actions workflow
├── LAB-REPORT.md
├── LICENSE                  # MIT
└── README.md
```

## Setup

Requirements: Python 3.8 or newer. No third-party packages are needed.

```bash
git clone https://github.com/haziqmirza812/student-task-manager.git
cd student-task-manager
```

## Usage

```bash
python main.py
```

```
===== Student Task Manager =====
1. Add task
2. Display tasks
3. Complete task
4. Delete task
5. Exit
```

Choose an option by typing its number. See [docs/user-guide.md](docs/user-guide.md) for a walkthrough.

## Running the tests

```bash
python -m unittest discover -s tests -v
```

The same command runs automatically in GitHub Actions (`.github/workflows/tests.yml`)
on every push to `main` and on every Pull Request targeting `main`.

## License

Released under the [MIT License](LICENSE).
