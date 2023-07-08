# Pandemic Crisis Management Simulation with AI

## Overview
This is an interactive and educational project designed to teach serious game development with AI. It provides a framework for creating grid-based games where players navigate through a world, encountering various challenges and obstacles. The game is implemented using Python and incorporates artificial intelligence techniques for character movement, decision-making, and problem-solving. It offers both a CLI and GUI for interacting with the game and modifying its behavior.

## Demo & Preview


## Prerequisites / Installation
To get started, ensure that you have Python 3.8 or higher installed on your system. You can check your Python version by opening the command prompt (Windows) or Terminal (macOS) and running python --version. If you have a version less than Python 3.8 or encounter an error, follow the instructions below to install Python version 3.8.5.

We recommend using Anaconda as your Python package manager. Anaconda comes with many required packages. Although we can provide an Anaconda environment file, it complicates the installation process. Instead, we will use pip (another Python package manager) to install the necessary packages that are not included in Anaconda.

Here are the steps for installation:

* Download [Anaconda](https://www.anaconda.com/) from the official website. Choose the latest version that includes Python 3.8 or higher.
* Install Anaconda, which will also install Python.
* Ensure that Git is properly set up on your system. If you need help with Git, refer to the [GitHub documentation](https://docs.github.com/en/github/getting-started-with-github/set-up-git).

After installing Anaconda, Python, and Git, you need to install additional packages using pip. Open the command prompt or Terminal and run the following command:
```shell
pip install tensorflow keras keras-rl2 gym>=0.2.3 pygame argparse uuid json xlrd pandas m
```

## Getting Started
Follow these steps to get started:
* Ensure that you have installed Python and the required packages by following the Prerequisites / Installation section above.
* Set up an SSH key between your computer and MIT GitHub. Refer to the [Git documentation](https://docs.github.com/en/enterprise-server@2.19/github/authenticating-to-github/connecting-to-github-with-ssh) for instructions.
* Clone the repository by running the following commands in the command prompt or Terminal:
```shell
git clone git@github.mit.edu:BWSI-SGAI-2021/SGW_MAIN.git
cd SGW
git status
```
These commands will clone the repository to your system, and you will see the repository files in the SGW directory. You can run Python files in the main directory to explore the game.

## Game Details
_Note:_ this repository contains the base classes (SGW) and the "Runner" files (RUN) that provide an interface between you and the game classes. The **Runner** files are the files you're supposed to modify and run.

The game is a command-line interface (CLI) game and can be run from a command prompt, terminal, or integrated development environment (IDE). The entry points for the code have "RUN" as a prefix.

For example, to run basic tests and view the available CLI options, use the following command:
```shell
python RUN_Basic.Tests.py -h
```
