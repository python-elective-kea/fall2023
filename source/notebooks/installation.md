# Installations

## Install python
Go to [www.python.org](https://www.python.org) and find the download button, and install python.
When done open you Terminal (mac) og Powershell (win) and type

```
	$ python3 --version
	Python 3.10.9
``` 
you should see something like this. 
If not, python is not installed, or maybe something else went wrong (ask Claus). 

## Install VS Code
Go to [code.visualstudio.com](https://code.visualstudio.com/) and find the download button for your operating system. Download and install VS Code. 

## Setup the development environment
1. Open VS Code.
1. Click on the "Extensions" icon in the left sidebar.
1. Search for "python" and install the Python extension from Microsoft.
2. Click on the "Source Control" icon in the left sidebar (the icon looks like a square with a branch).
3. In the "Source Control" panel that appears at the left side of the window, click on the "Clone Repository" button.
4. A textbox will appear asking for the repository URL. 

   Enter 
```
   https://github.com/python-elective-kea/fall2023-code-examples-from-teachings.git
``` 
   
and press Enter.

5. Choose a local folder on your computer where you want to clone the repository and click "Clone".
6. Once the repository is cloned, click on the "Explorer" icon in the left sidebar (the icon looks like a square with a folder).
1. In the "Explorer" panel, navigate to the folder where you cloned the repository (e.g., `fall2023-code-examples-from-teachings`). 
1. In the bottom-left corner of the VS Code window, you should see the Git status bar. If it's not visible, you can enable it by clicking on the "Source Control" icon in the left sidebar.
1. Click on the branch name currently displayed in the Git status bar (usually the default branch name, such as "main" or "master").
1. In the branch dropdown, type "playground" and press Enter to create a new branch named "playground". Alternatively, you can click on the "+" icon to create a new branch and enter "playground" as the branch name.
1. Once the branch is created, the Git status bar should now display "playground" as the active branch.
1. Find the playground.ipynb file in the project folder within the "Explorer" panel.
1. Find the `playground.ipynb` file in the folder and double-click on it to open it in the VS Code editor.
9. In the top right corner click on:
   
```
   * Select Kernel -> 
   * Python environmets -> 
   * Create Python Environment -> 
   * Venv Create a '.venv' virtual envitonment in the current workspace -> 
   * Python 3.11.3 (or another version)
```
10. This will create a '.venv' in your folder, which is a virtual python installation with the dependencies needed for running the projekt.

### The code and exercises files the rest of this semester
In the future, this is how you should work on the files and exercises given to you in teachings. 
You should `pull` the master branch when new files are added to the respoitory, and then create a new branch where you can play around with the files or do the exercises. And you should never merge your branches into the master branch. 

!! IMPORTANT. Do not edit any files directly in the master branch, it should be keept clean. Othervise you will end up with a lot of merge errors.

