---
layout: default
title: 1. Linux command Line
nav_order: 2
---


# The Linux command line for beginners

## Motivation

The command line is an alternative to the GUI based interface you are so used to. Although GUI interfaces are quite easy to use, they are not as flexible and powerful as the command line. For simple operations, the GUI is probably favourable. However, the command line has several distinct advantages: (1) More complex operations can be performed, such as searching through thousands of files for a specific string and copy these files, or easily transferring files between your computer and a remote server. Secondly, (2) the command line is typically faster than a GUI since there is less overhead from the graphical user interface; (3) servers such as HPC clusters typically do not offer a graphical user interface, so the command line is the only way to operate there; and (4) commands can be scripted easily in order to automate tasks and complex operations.

The Linux shell can be accessed by programs like the terminal. They come with a long list of commands by default which can be combined to build larger programs from smaller ones is what gives the command line its power and flexibility.

In this lesson you learn about some of the most useful commands.

## Opening a terminal

On a Debian 11, which is the version of the linux operating system used in the computer labs, you can find a launcher for the terminal by clicking on the **Applications** item at the top left of the screen, then **System Tools**, and there you will find an entry called **MATE Terminal**.

> **Note:** There are many different terminal versions installed, such as **LXTerminal**, **Terminator**, or **Xfce Terminal**. Except for some functionality and different design, they work all the same.

This video explains the design of the shell and the following aspects:

- The *working directory* is the directory, which the terminal is currently looking at.
- The `~` symbol is a special directory shortcut refering to your `home` directory.

<video width="640" height="480" controls preload="metadata" controls poster="videos/terminal-introduction-1.png">
  <source src="videos/terminal-introduction-1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## Folder directories

Managing your directories and file structure in your computer or servers is an important skill you need to use when running CFD simulations on linux machines and HPC cluster. In this concept, we are going to show you how to use the terminal with multiple commands to navigate and organize your files.

This video focuses on the following topics:
- Listing the content of a directory using `ls`. Additional information can be shown when using the additional argument `-l`.
- Changing the working directory using the command `cd`.

[Video: terminal-introduction-2.mp4]

## Current working directory

Sometimes you will get lost in many directories, with this command you can see where you are.

This video explains the following topics:
- Print out the current working directory using `pwd`.
- Special directory names are introduced: `..` stands for the parent directory; `.` for the current directory, and `~` for the home directory.

[Video: terminal-introduction-3.mp4]

## Organizing your files

With the terminal, you can use commands to organize your files into directories, move files, copy or remove the files.

This video emphasizes on the following topics:

- Creating new directories with `mkdir`.
- Move files and folders around or rename them using `mv`.
- Introduction of the wildcard `*`, which stands for one or more occurrences for any character.

[Video: terminal-introduction-4.mp4]

## Viewing files

With the terminal, you can use commands to view files, let's learn how to do it in this concept.

This video focuses on the following topics:

- Viewing files using `cat`, `less` and the top and bottom lines with `head` and `tail`, respectively.

[Video: terminal-introduction-5.mp4]

## Removing files or directories

With the terminal, you can use commands to remove files or directories.

This video shows the following aspects:

- Copying single files using `cp` and directories recursively with the additional argument `-r`.
- Deleting files with `rm` and directories recursively using the additional argument `-r`.
- Deleting the content of all files and directories within a given directory using the wildcard `*`

[Video: terminal-introduction-6.mp4]

> **Warning:** The `rm` command deletes files and directories without a waring and without using the Recycle Bin or Trash Can. Therefore, these files cannot be recovered. Be particularly careful when combining this command with wildcards, as complete folders and be deleted easily by mistake
