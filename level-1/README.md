
## 🛰 Operation Starbase Recovery

## Mission Brief

A meteor storm damaged **Starbase Orion**, causing the automated backup system to fail.

Critical files have been scattered throughout the station, corrupted files remain, and the filesystem is no longer organized.

Mission Control has tasked you with restoring the station before launch.


## Mission Objectives

All required tasks are documented in the **Mission Log**.

Your mission is to:

-   Read the Mission Log.
-   Determine what needs to be repaired.
-   Restore the filesystem.
-   Verify your work.

----------

## Mission Rules

-   Use only the Linux terminal.
-   Do not rename files.
-   Do not edit file contents.
-   Only remove files identified as corrupted.
-   Remove empty folders when they are no longer needed.
-   Do not modify the verification script.

----------

# Helpful Linux Commands

These examples demonstrate the **syntax** of each command. They are **not** the solution to this lab.

Command

Purpose

Example

`pwd`

Display your current working directory.

`pwd`

`ls`

List files and folders.

`ls`

`ls -la`

Show detailed file information, including hidden files.

`ls -la`

`cd`

Change directories.

`cd Documents`

`cd ..`

Move up one directory.

`cd ..`

`cat`

Display the contents of a text file.

`cat notes.txt`

`mkdir`

Create a new directory.

`mkdir Projects`

`mv`

Move a file or folder.

`mv report.txt Projects/`

`cp`

Copy a file.

`cp report.txt backup.txt`

`rm`

Delete a file.

`rm old_notes.txt`

`rmdir`

Remove an empty directory.

`rmdir Temp`

`find`

Search for files or folders.

`find . -name "*.txt"`

`clear`

Clear the terminal screen.

`clear`

----------

## Understanding Command Syntax

Many Linux commands follow this pattern:

```
command [options] [source] [destination]
```

Example:

```
mv report.txt Documents/
```

-   **Command** — What action Linux should perform.
-   **Options** — Additional settings (optional).
-   **Source** — The file or folder you're working with.
-   **Destination** — Where the item should be moved.

----------

## Helpful Resources

-   Linux Journey — [https://linuxjourney.com](https://linuxjourney.com)
-   Explainshell — [https://explainshell.com](https://explainshell.com)
-   Linux Manual Pages — [https://man7.org/linux/man-pages/](https://man7.org/linux/man-pages/)

----------

## Mission Completion

When you believe the station has been restored, run:

```
python verify.py
```

or

```
python3 verify.py
```

Mission Control will inspect your work.

Good luck, Commander.
