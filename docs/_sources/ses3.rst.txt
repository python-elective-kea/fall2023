Session 4 - Modules & list comprehensions
=========================================
Today we will examine modules in Python. You will create your own modules and learn how to use Python's built-in modules. In two weeks, we will continue with 3rd party modules (code created by others) and you will learn how to incorporate these into your own code and ensure that others using your code have access to the same 3rd party modules and the correct versions.

First, we will examine list comprehensions, a concise way to generate lists.

Today on the practical level, you will work with four modules in addition to comprehensions:

* Os module
* Subprocesses module
* zipfile module
* Requests module

Learning goals
--------------
After this week you will be able to:
       
        - Use listcomprehensions.
        - Create your own modules.
        - Use Python's built-in modules.
        - Find and use 3rd party modules.
        - Use the requests module to fetch website data.

Materials
---------
* `Comprehending Python’s Comprehensions <https://dbader.org/blog/list-dict-set-comprehensions-in-python>`_
* `Python Modules and Packages <https://realpython.com/python-modules-packages/>`_
* `Working With Files in Python <https://realpython.com/working-with-files-in-python/#making-directories>`_
* `Subprocess management <https://docs.python.org/3.7/library/subprocess.html#module-subprocess>`_
* `Python’s Requests Library <https://realpython.com/python-requests/>`_
* `Downloading Files from URLs in Python <https://www.codementor.io/aviaryan/downloading-files-from-urls-in-python-77q3bs0un>`_ 
* `Notebook <notebooks/Notes-Contextmanager-ListComp-modules.ipynb>`_
* `Code examples from teachings <https://github.com/python-elective-kea/fall2023-code-examples-from-teachings/tree/master/ses3>`_

Exercises
---------

**List Comprehensions**

----------------------------------
Ex 1: Alphabet List Comprehensions
----------------------------------
`Solution <exercises/solution/03_os_sub_req/solutions.rst#ex-1-alphabet-list-comprehensions>`_

1. Create a list of capital letters in the english alphabet
2. Create a list of capital letter from the english aplhabet, but exclude 4 with the Unicode code point of either 70, 75, 80, 85.
3. Create a list of capital letter from from the english aplhabet, but exclude every second between F & O

--------------------------------
Ex 2: Clothes List Comprehension
--------------------------------

`Solution <exercises/solution/03_os_sub_req/solutions.rst#ex-2-clothes-list-comprehension>`_

1. From 2 lists, using a list comprehension, create a list containing:


        [('Black', 's'),
        ('Black', 'm'),
        ('Black', 'l'),
        ('Black', 'xl'),
        ('White', 's'),
        ('White', 'm'),
        ('White', 'l'),
        ('White', 'xl')]


.. code::
   :linenos:

        colors = ['Black', 'White']
        sizes = ['s', 'm', 'l', 'xl']

2. If the tuple pair is in the following list, it should not be added to the comprehension generated list. 

.. code::
   :linenos:

        soled_out = [('Black', 'm'), ('White', 's')]

 
..      ----------------------------
        Ex 3: List & tuple exercises
        ----------------------------
        `Solution <exercises/solution/03_os_sub_req/solutions.rst#ex-3-list-tuple-exercises>`_

        Based on these exercises from last time, solve the exercises by using list comprehensions instead. 

        * `List & tuple exercises <exercises/lists/lists.rst>`_

  
----------------------------------
Ex 3: list Comprehension exercises
----------------------------------

1. Create a list of even numbers from 0 to 20.
2. Create a list of squares of numbers from 1 to 10.
3. Create a list of all the vowels in a given string.
4. Create a list of common elements in two given lists.  
5. Create a list of words from a given string that have more than 4 letters.

**Modules**

------------------------
Ex 5: OS Module exercise
------------------------

`Solution <exercises/solution/03_os_sub_req/solutions.rst#ex-5-os-module-exercise>`_

.. literalinclude:: exercises/util_modules/os_exercise.py
        :linenos:

..       -----------------------
        Ex 6: Extract .py files
        -----------------------
        `Solution <exercises/solution/03_os_sub_req/solutions.rst#ex-6-extract-py-files>`_

        Create a program (a function) that when run takes 1-3 arguments where:

        | * the first is the name of a directory in play
        | * the second (optional) is a --flag (--todir <dirname>) that specifies where the files in that directory should be copied to.
        | * the third (optional) is a --flag (--zip <filename>) that specifies if the files should be zipped and what the zip file should be called.

        So if you run the program like this :code:`python extract.py . --todir /tmp/ --zip archive.zip` you should copy all files in the current directory (.) to a new tmp directory and the .py files should be put in a zip folder names archive.zip.


        Task A:
        *******
        Copy all .py files in a given directory to a new folder.

        Task B:
        *******
        Zip all .py files in a given directory and put the zip file in the specified folder.

----------------------------------
Ex 7: Simple scraber with requests
----------------------------------

`Solution <exercises/solution/03_os_sub_req/solutions.rst#ex-7-simple-scraber-with-requests>`_

| 1. Create an application that asks for an url. 
| 2. Then Download that html page, and its images, icons etc. and change it so it will work locally on your computer. Locally means that you should be able to cut your internet connection and still have a functionig html page. 
| 3. When done push all files to your github account. (all should be done programattically) Hint: api.github.com/user/repos can be used to create a repository from you program on Github)

| You will have to use the requests module, the OS module and the subprocesses module for this taks.
| An easy website to scrape is this: 

------
quizes
------
* `HTTP Requests With the "requests" Library Quiz <https://realpython.com/quizzes/python-requests/>`_


