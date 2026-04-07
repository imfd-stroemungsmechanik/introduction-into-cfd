---
layout: default
title: Gnome Desktop
parent: 1. Linux Introduction
nav_order: 1
---

# The Gnome Desktop

For this seminar, we are using the **Debian 13** operating system with the **GNOME** desktop environment. 

If you are coming from Windows, Linux will look and feel a bit different. In Windows, the operating system and the graphical interface are one tightly integrated package. In Linux, they are separate. Debian handles the underlying system (managing files, hardware, and running OpenFOAM), while GNOME is the "face" of the system—the windows, buttons, and menus you interact with.

Here is a quick guide to navigating GNOME and where to find everything you are used to in Windows.

## Comparison between Windows and Gnome

| Windows Feature | GNOME Equivalent | How to access it |
| :--- | :--- | :--- |
| Start Menu | Activities Overview | Press the `Super` key (the Windows key on your keyboard) or click "Activities" in the top left. |
| Taskbar | The Dash (Dock) | Press the `Super` key. The dock appears at the bottom of the screen. |
| Windows Explorer | Files (Nautilus) | Open the "Files" app from the Dash or App Grid. |
| System Tray (Bottom Right) | Quick Settings (Top Right) | Click the top-right corner of the screen (Wi-Fi, sound, power). |
| Command Prompt / PowerShell | Terminal | Press `Super`, type "Terminal", and press Enter. |



## Key Features of GNOME

### The "Activities" Overview and the Super Key
GNOME is designed around minimizing distractions. When you log in, you will see an empty desktop. There are no desktop icons and no traditional Start button. 
Everything revolves around the **Activities Overview**.

*   **How to use it:** Press the **`Super` key** (the key with the Windows logo) or click the top-left corner of the screen.
*   **What it does:** The screen zooms out. You will see all your open windows, your workspaces, the search bar at the top, and the **Dash** (dock) at the bottom.
*   **How to launch apps:** Simply press the `Super` key and start typing. To open the terminal, press `Super`, type `term`, and hit `Enter`. This is the fastest way to work.

### The File Manager
Managing your simulation directories is crucial in OpenFOAM. The GNOME file manager is simply called **Files**.
*   **No "C:\" Drive:** Linux does not use lettered drives. Everything starts at the "root" directory, denoted by a forward slash `/`. 
*   **Your Home:** Your personal files are stored in your Home directory (`/home/username/` or simply `~`). When you open the Terminal, it automatically starts here.
*   **Hidden Files:** In Linux, any file or folder that starts with a dot (e.g., `.bashrc`) is hidden. **To view hidden files in GNOME, press `Ctrl + H`.** You will need this shortcut later when configuring your OpenFOAM environment!

### Workspaces (Virtual Desktops)
CFD workflows can get cluttered quickly. You might have one window for your Terminal (running the simulation), one for ParaView (visualizing the results), and a web browser open to this tutorial.
*   GNOME uses **Workspaces** to help you organize. 
*   Press the `Super` key and look at the top (or right side) of the screen to see your workspaces. You can drag and drop open windows into different workspaces to keep your Terminal separate from your visualization tools.
*   **Shortcut:** Switch between workspaces quickly by pressing `Super + PageUp` or `Super + PageDown` (or using a three-finger swipe on a touchpad).

### Quick Settings
Need to connect to the university Wi-Fi, adjust the volume, or shut down the computer? Click the group of icons in the **top-right corner** of the top bar. This opens the Quick Settings menu, which is similar to the Windows Action Center.