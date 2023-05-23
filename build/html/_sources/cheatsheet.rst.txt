Commandline Cheatsheet
======================
In this cheatsheet you will find important and hard to remember terminal commands.

Docker Commands
---------------

---------------------------------
Session 1 - Introduction to python 
---------------------------------

.. code::
   
   $ docker run -it --rm ubuntu:20.04  // creates and runs a simple ubuntu container with interactive access and removal after use. 
   $ docker run -it --rm python:3.10.1 bash // same as above, but now a python image. starts in a bash terminal.
   $ docker run -it --rm -v ${PWD}:/docs python:3.10.1 bash  // same as above, but now sharing files from the current directory to/from /docs folder in the container.
 
----------------
Creating aliases
----------------

Typing in these long lines of commands can be overvelming, and in many cases it will result in many of you not using Docker at all for the execution of your python scripts.     

The solution for this is creating aliases in you shell configuration files.

===
Mac
===

Depending on which shell you are using do the following. 


.. code::
   
   # First check which shell you are using. 
   $ echo $0
   # -> result will be bash or zsh

   $ cd ~                 # move to root folder
   $ open .bash_profile   # if you are using bash (if you get an error, create it first)

   $ open .zsh_profile    # if you are using zsh (if you get an error, create it first)

   # copy/paste this in
   $ alias dk_python='docker run -it --rm -v ${PWD}:/docs python:3.10.1 bash'  


Now in your terminal you should be able to write **dk_python** instead of the long docker command 

=======
Windows
=======

First you should open your powershell in administrator mode.      
Then copy/paste this in:

.. code::

   > set-executionpolicy remotesigned

This will allow execution of scripts in your powershell. 

Then copy paste this in:

.. code::

   > notepad $((Split-Path $profile -Parent) + "\profile.ps1")

This will open a file. Copy/paste this in:

.. code::

   > Set-Alias dk_python 'docker run -it --rm -v ${PWD}:/docs python:3.10.1 bash'


Now in your Powershell you should be able to write **dk_python** instead of the long docker command 


---------------------------------
Session 5 - Utilities and Modules
---------------------------------

.. code::

        $ docker build --tag webscrabing:latest .
        $ docker run -it --rm -v ${PWD}:/docs webscrabing 

----------------------------------
Session 9 - Functions & Decorators
----------------------------------

.. code::

        $ docker run --name jupyter -p 8888:8888 -v ${PWD}:/home/jovyan/work  jupyter/base-notebook 

---------------
Sphinx commands
---------------

.. code::
   
   $ docker run --rm -v ${PWD}:/docs sphinx /bin/sh -c 'cd sphinx/; make html'


