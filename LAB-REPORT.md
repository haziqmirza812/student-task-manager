# Lab Report – Assignment 4

**Course:** CSC418 DevOps for Cloud Computing  
**Project:** Student Task Manager – development and version control using Git and GitHub  
**Repository:** https://github.com/haziqmirza812/student-task-manager

## 1. Git vs GitHub; purpose of add, commit and push

**Git** is a version control tool that runs on my own computer. It records snapshots of my
files, so I can see what changed, go back to an older version and work on branches.
**GitHub** is a website that hosts Git repositories online. It adds collaboration features on top
of Git: Issues, Pull Requests, code review, GitHub Actions and Releases.

- `git add` puts selected changes into the *staging area*, i.e. it chooses what goes into the next commit.
- `git commit` saves the staged changes as a permanent snapshot in the local history, with a message that explains *why*.
- `git push` uploads my local commits to the remote repository on GitHub so others (and CI) can see them.

## 2. Why branches and Pull Requests are used; what causes merge conflicts

A **branch** is an independent line of development. I built each feature
(`feature/add-task`, `feature/complete-task`, `feature/delete-task`) on its own branch, so unfinished
work never broke `main`, and each feature could be reviewed and merged separately.

A **Pull Request** asks to merge one branch into another. It shows the changed files, lets
reviewers comment, runs the automated tests, and links to the Issue it solves (`Closes #1`), so the
history explains why every change was made.

A **merge conflict** happens when two branches change the *same lines* of the same file in different
ways (or one deletes what the other edits). Git cannot decide which version is correct, so it stops
and inserts conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`) for a person to resolve. In Part D, both
`status/in-progress` and `status/testing` edited the line `Project status: Planning` in README.md.

## 3. fetch vs pull; merge vs rebase

- `git fetch` downloads new commits from the remote but does **not** change my working files or current
  branch; I can inspect them first.
- `git pull` = `git fetch` **+** integrate (merge by default) into my current branch in one step.

- **Merge** joins two branches by creating a merge commit. The full history, including where branches
  split and joined, is kept (non-linear graph).
- **Rebase** re-applies my commits on top of another branch, producing a straight, linear history,
  but it rewrites commit IDs, so it should not be used on branches others already share.

## 4. How GitHub Issues and Actions help a team

**Issues** are a shared to-do list: each bug, feature or documentation task has a description,
labels (enhancement, testing, documentation), an owner and a discussion. Linking an Issue from a PR
closes it automatically on merge, so the team always knows what is done and why.

**GitHub Actions** runs automation on GitHub's servers. My workflow runs the unit tests on every push
and Pull Request to `main`. A broken change shows a red ❌ before it is merged (I demonstrated a failed
run on purpose and then fixed it), so nobody has to remember to run tests by hand.

## 5. One difficulty and how I solved it

My first working environment had no GitHub credentials, so `git push` was rejected with a 403 error.
I solved it by doing the Git work inside a **GitHub Codespace**, which is automatically signed in to my
GitHub account, so pushes, branches and Pull Requests worked without storing a password or token.

A smaller one: after fixing the deliberately wrong assertion in `test_delete_task`, my local test run
still showed the old failure because of a stale `__pycache__` file. Deleting `tests/__pycache__` fixed it,
and the Python `.gitignore` keeps these cache files out of the repository.
