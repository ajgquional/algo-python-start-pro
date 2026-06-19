# Python Start (Year 1 and 2) and Python Pro (Year 2) by Algorithmics

## Description

This repo contains materials (mostly Python scripts) for the activities in the Python course of Algorithmics International School of Programming. Specifically, this repo contains materials from Python Start (Year 1 and 2) and Python Pro (Year), covering basic to advanced Python topics. This is intended for instructional purposes and as a student reference. Also, this repo is created to serve as a standalone reference to teach the course/s along with the standard VS Code (not Algo VS Code). Most of the materials are obtained from Algorithmics, with personal corrections and supplements added to simplify the activities. With that said, no copyright infringement is intended.

## Structure

The repo contains the whole series of courses and is ordered by module number from basic to advanced Python topics, with no separation from "Python Start" to "Python Pro" topics. However, for reference, here's the structure (based from the Algorithmics LMS) considering which topics fall in Python Start (Year 1 and 2) and Python Pro (Year 2):

- Python Start (Year 1)
    - 1 - Python Basics
    - 2 - Control Structures
    - 3 - Functions and Modules (to be added)
    - 4 - Turtle Module, Math for Developer (to be added)
    - 5 - Object-oriented Programming (to be added)
    - 6 - PyGame Game Development Basics (to be added)
    - 7 - Hackathon Series (no material)
    - 8 - Graduation (no material)

- Python Start (Year 2)
    - 9 - Data Structures
    - 10 - Development of Windowed Applications
    - 11 - Work with Text Files
    - 12 - Automatic Image Processing
    - 13 - Advanced Game Development using PyGame
    - 14 - Publishing and Distributing Software (see this <a href="https://github.com/ajgquional/ping-pong-game-algo" target="_blank">repo</a>)
    - 15 - Graduation Series (no material)

- Python Pro (Year 2)
    - 16 - Review
    - 17 - Mobile Development
    - 18 - Data Analysis (to be added)
    - 19 - Basics of Machine Learning (to be added)
    - 20 - 3D Games (to be added)
    - 21 - Web Development (to be added)
    - 22 - Career for Python Developer (no material)

## Usage

Since this repo is independent of the Algo VS Code, below are the recommended steps for setting up before using the scripts (it is assumed that a Windows machine is used):

1. Install VS Code from https://code.visualstudio.com/. 
2. Install <a href="https://www.python.org/downloads/release/python-3913/" target="_blank">Python 3.9.13</a> for Windows (choose the correct installer at the bottom, either for 64-bit or 32-bit), available from the official Python website. (The course is created using Python 3.9.13 so the same version must be installed, albeit already reached end-of-life. Other later versions can perhaps be used but the scripts are not guaranteed to work since package versions might need updating.)
3. Create a project folder then navigate to it via:

```bash
cd path\to\project
```

Alternatively, if you have a GitHub account, this repo can be cloned in a suitable location within the local computer:

```bash
git clone https://github.com/ajgquional/algo-python-start-pro.git
```

After cloning the repo, navigate to it using the same command:

```bash
cd path\to\project
```

4. Once Python is installed and navigated to the project folder, it is recommended to create a virtual environment (for safer package installations) in the project folder before installing the needed packages for all scripts to work. Assuming there's only one Python version installed, use the following command to create the virtual environment (via `venv`):

```bash
python -m venv algovenv
```

If there are multiple Python versions installed, list first all available Python versions:

```bash
py -0
```

Example output:

```bash
Installed Pythons found by py Launcher:
 -V:3.10
 -V:3.9
```

Create the virtual environment using Python 3.9:

```bash
py -3.9 -m venv algovenv
```

5. Activate the virtual environment. 

### Option 1: Using PowerShell

```bash
.\algovenv\Scripts\Activate.ps1
```

If PowerShell shows an error similar to:

```bash
running scripts is disabled on this system
```

run the following command once:

```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

then activate the virtual environment again:

```bash
.\algovenv\Scripts\Activate.ps1
```

### Option 2: Using Command Prompt (cmd)

```bash
algovenv\Scripts\activate.bat
```

To verify successful activation of the virtual environment, you should see:

```bash
(algovenv)
```

at the beginning of the terminal prompt.

To deactivate the virtual environment, use

```bash
deactivate
```

6. Install dependencies (packages) after activating the virtual environment:

```bash
pip install -r requirements.txt
```

Verify installed packages using

```bash
pip list
```

Check for dependency issues:

```bash
pip check
```

7. Lastly, while still in the terminal, open VS Code via

```bash
code .
```

Automatically, the activated virtual environment would be carried over to the terminal of VS Code. Also, when VS Code is closed then opened again, normally, the previous session (activated virtual environment in the terminal) is remembered. In this case, there's no need to manually open the virtual environment again. If it is needed, follow Step 5.

## Current Status

- Working on Modules 20 and 21

## TODO

- To add Modules 3-6, 18-19
- To add IL (Introductory Lesson) sample projects
- Future: Replicate some scripts (for faster demo purposes) in an open web platform for Python coding (possibly Replit)
