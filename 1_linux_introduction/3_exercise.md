---
layout: default
title: Exercise
parent: 1. Linux Introduction
nav_order: 3
---


# Exercise

While the GNOME graphical interface is suitable for general tasks, OpenFOAM relies entirely on the **Terminal** (the command-line interface). To facilitate the transition to this workflow, the following exercise bridges the gap between graphical file management and terminal commands.


## Part 1: Graphical File Management

The workspace must first be prepared using the graphical interface. OpenFOAM simulations are organized into "cases," which are essentially directories (folders) containing specific configuration text files.

1. Download the archive file [1_linux_introduction.zip](https://github.com/user-attachments/files/26598622/1_linux_introduction.zip) containing a dummy OpenFOAM case repository.
2. Open the File Manager by pressing the `Super` key, type `files`, and press `Enter`.
3. Extract the archive:
   * Navigate to the **Downloads** directory.
   * Right-click `1_linux_introduction.zip` and select **Extract Here**.
4. Organize the workspace: 
   * Select **Home** from the left sidebar.
   * Right-click in the empty space, select **New Folder**, and assign the name `OpenFOAM_Projects`.
   * Return to the **Downloads** directory, copy the extracted `1_linux_introduction` folder, and paste it into the newly created `OpenFOAM_Projects` folder.

The mock simulation directory has now been downloaded, extracted, and organized using the graphical user interface. The next section demonstrates how to interact with this exact same directory using the Terminal.



## Part 2: Terminal Interaction

Execute the following commands sequentially in the Terminal, pressing `Enter` after each line. Read the accompanying explanations to understand the function of each command.

#### Verify the current location
```bash
pwd
```
This confirms the Terminal is operating within the Home directory. This is the exact same location as clicking **Home** in the graphical file manager.


#### View directory contents with details
```bash
ls -l
```
Adding the -l (long) flag to the ls command displays the directory contents in a detailed list, showing permissions, ownership, and modification dates. The newly created OpenFOAM_Projects directory will be visible here.

#### Navigate using Tab Completion

Typing long directory names is inefficient. Instead, type the first few letters and use auto-complete.

```bash
cd OpenFOAM_Projects
```

#### Enter and inspect the case directory

```bash
cd 1_linux_introduction
ls
```

Running `ls` here will display three items: `0`, `constant`, and `system`. This is the strict standard directory structure required for every OpenFOAM case.

#### Create a case backup

In CFD workflows, duplicating a working case before modifying the setup is standard practice. To copy an entire directory, the `-r` (recursive) flag must be included.

```bash
cd ..
cp -r 1_linux_introduction 1_linux_introduction_backup
ls
```

#### Rename the backup directory

The `mv` (move) command is dual-purpose: it moves files to new locations, but it is also the standard way to rename files and directories.

```bash
mv 1_linux_introduction_backup 1_linux_introduction_v2
ls
```

The backup directory has now been renamed to 1_linux_introduction_v2.

#### Delete a directory

If a simulation setup fails, the directory often needs to be deleted. The `rm` (remove) command handles this. Similar to copying, deleting a directory requires the `-r` flag.

```bash
rm -r 1_linux_introduction_v2
ls
```

{: .warning }
> Terminal deletion is permanent. Files removed with `rm` do not go to a graphical trash bin.

#### Inspect a configuration file

OpenFOAM does not feature a graphical setup menu. Simulation parameters are defined in text files, often called "dictionaries" or "dicts".

```bash
cd 1_linux_introduction
cat system/controlDict
```

#### Clean up the workspace

To finalize the exercise, the terminal screen can be cleared of all previous command output.

```bash
clear
```

The terminal is now reset to a blank slate, ready for the next task.