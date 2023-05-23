# Installations

## Last minutes change to the installation process.
Previous semesters we installed python through Docker Desktop i the first sessions of the semester. We will pospone this for a few weeks.
Instead you should today install python directly on your computer.

## Install python
Go to [www.python.org](https://www.python.org) and find the download button, and install python.
When done open you Terminal (mac) og Powershell (win) and type

```
	$ python3 --version
	Python 3.10.9
``` 
and you should see sometthing like this. If not python is not installed, or maybe something else went wrong (ask Claus). 



### The things described beneath will be used at a later session this semester but not today

This document will describe what you should install in order to follow this elective.   


You will not install python directly on your computer, but instead run docker containers build open different kinds of python images.    

The benefit of this approach is that we all, no matter what OS we normally use, can use the exact same development environment, and have the exact  same dependencies installed for our applications.  
This makes it easier to work together across different OS in groups (at work or in class). It also will teach you how to work with an industry standard, so you know this development environment and approach when you start to work after your education has ended.  




You probably already have installed some of the following applications, but if you do not you should now install:


1. Docker desktop 
2. Some kind of text editor.
3. Git 
4. Create a GitHub account.


## 1. Docker Desktop
### Download and install Docker Desktop

Navigate to the Docker website and download and install Docker Desktop for your operating system.   

[Docker Desktop download](https://www.docker.com/products/docker-desktop)    

## Windows Home 10 users
On Windows Home 10 you could run into some trouble while installing Docker.     
Follow these steps to solve these problems.     
[Install Docker Desktop on Windows Home](https://docs.docker.com/docker-for-windows/install-windows-home/)

#### Check if everything is installed
In your terminal or powershell you should type ``` docker --version ``` and get the following result.

````
	$ docker --version 
	Docker version 20.10.17, build 100c701
````
If you do not see this, get an error or like, then you still de not have docker installed on your system.

### Run your first Docker container (Ubuntu). 

The first Image you should create a container from is a basic Ubuntu image.    

Run the following command in your termianl to download the image and run a container.




````
	$ docker run -it --rm ubuntu
````
With:   

* <b>-it</b>: you specify to run the container in interactive mode (you can use its terminal).
* ** --rm **: you specify that the container should be deleted when you exit the terminal.
* ** ubuntu ** : is the name of the image
 
After downloading has finnished, and run has executed you should see something like this in your terminal.

````
	$ docker run -it --rm ubuntu
	root@710ef1a882be:/#
````

Now you have a ubuntu operating system running on your computer (in a docker container).


### Run your Second Docker container (Python). 
The second image you should create a container from is the official Python Docker image.
To download the image and run a container, run the following command in your terminal:

````
	$ docker run -it --rm python:3.9.13 bash
````

With:   

* -it:  
	* you specify to run the container in interactive mode (you can use its terminal).
* --rm: 
	* you specify that the container should be deleted when you exit the terminal.
* python: 
	* is the name of the image.
* bash: 
	* specifies that you want to start the container with a terminal gui (bash) 

After downloading has finnished, and run has executed you should see something like this in your terminal.

````
	$ docker run -it --rm python:3.9.13 bash
	root@a7991e5db4cd:/#
````

Now you have an linux operating system running on your computer with some version of python installed in it (in a docker container).   

In the terminal you now have open type in the following:    

````
python --version
````

When pressing enter, you should now see the following

````
python --version
Python 3.8.2
````

## 2. Download and install a text editor
Download and install a text editor. There are many good ones, and you need at least one, but you decide which one.   

### VS Code
A good option is VS Code. You can download it from the following source: 

* [https://code.visualstudio.com/](https://code.visualstudio.com/)

**The recomendation for this elective is to use VS Code.**

#### Other popular text editors are:
* Atom
* Sublime Text
* Notepad++
* Vim

#### IDE´s
You could also choose to use an IDE instead of a text editor. 

Jetbrains has an IDE called [PyCharm](https://www.jetbrains.com/pycharm/) which is a good choice, but you could also use other ones like IntelliJ of Visual Studio e.i. 

**NOTE:**  Using an IDE gives you a more automated workflow than using a text editor. But an IDE does not in this class support the learning goals as well as if you use the more manual approach with a text editor and a CLI (command line interface). So even though it will seam like an easier development environment, an IDE will be a more difficult approach in order to fulfill the learning goals, or in worst case you will not even notice that you did not learn what you should before it is to late. So in this elective the recomendation is to us VS Code.  


## 3. Git & Github
### Download and install Git
* If you do not already have git installed on your computer you should do this now. 

* [https://git-scm.com/](https://git-scm.com/) 

_If you are on **Windows** be sure to install the "Git Bash" (this is an option you can choose during the installation process.)_

#### Check if everything is installed
* Open you terminal and type in the following

````
git --version
````
When pressing enter, you should now see the following

````
git --version
git version 2.10.1  // or some other version number
````

If you see something else, Git is not installed correct, and you should try again.


## 4. Create a Github Account
* If you do not already have a GitHub account, you should create one now. 
    * Go to https://github.com/ and create an account 


