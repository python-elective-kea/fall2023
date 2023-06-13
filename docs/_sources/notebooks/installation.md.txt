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
2. Click on the "Source Control" icon in the left sidebar (the icon looks like a square with a branch).
3. In the "Source Control" panel that appears at the left side of the window, click on the "Clone Repository" button.
4. A textbox will appear asking for the repository URL. Enter `https://github.com/python-elective-kea/fall2023-code-examples-from-teachings.git` and press Enter.
5. Choose a local folder on your computer where you want to clone the repository and click "Clone".
6. Once the repository is cloned, click on the "Explorer" icon in the left sidebar (the icon looks like a square with a folder).
7. In the "Explorer" panel, navigate to the folder where you cloned the repository (e.g., `fall2023-code-examples-from-teachings`).
8. Find the `exercise.ipynb` file in the folder and double-click on it to open it in the VS Code editor.
9. Now, let's set up the environment based on the `.venv` folder:
   - Click on the "Extensions" icon in the left sidebar (the icon looks like four squares connected by lines).
   - In the search bar at the top of the "Extensions" panel, type "Python" and press Enter.
   - Look for the "Python" extension by Microsoft in the search results and click on the "Install" button.
   - After the installation, click on the "Reload" button to activate the extension.
10. With the `exercise.ipynb` file open, click on the "Run and Debug" icon in the left sidebar (the icon looks like a play button inside a bug).
11. At the top of the window, you'll see a dropdown menu labeled "Python" with options to select the Python interpreter. Click on it.
12. In the dropdown menu, select the option that corresponds to the `.venv` folder in the cloned repository. It may be named something like "Python [project-name]: .venv".
13. Once you select the Python interpreter, click on the green play button next to the dropdown menu to start the notebook kernel using the selected interpreter.
14. Now, you should be able to run and interact with the `exercise.ipynb` file in the VS Code notebook environment.

