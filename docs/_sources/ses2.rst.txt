Session 2 - Data Structures: List & Tuples
==========================================

Today we will work with data structures in python. You will by the end of these sessions be able to use Lists and Tuples, read and Write to Files and work with the **for** and **while** loop.

List and tuples are two of the build-in datastructures in python.

Learning goals
--------------

After this week you will be able to:
        
        - Work with lists, tuples
        - Loop over sequences with a for, foreach & while loops.  
        - Sort sequences using the build in sorted function and use its key parameter to perform custom sorting.  
        - Read from files and write to files using the build in "open" function. 

Materials
---------

* `Lists and Tuples in Python <https://realpython.com/python-lists-tuples/>`_
* `Tuples in Python <https://www.datacamp.com/community/tutorials/python-tuples>`_
* `Python "for" Loops <https://realpython.com/python-for-loop/>`_
* `Python "while" Loops <https://realpython.com/python-while-loop/>`_
* `How to Use sorted() and not .sort() in Python <https://realpython.com/python-sort/>`_
* `Notebook (teachings notes from today) <notebooks/noterlists_tuples.ipynb>`_
* `Code examples from teachings <https://github.com/python-elective-kea/fall2023-code-examples-from-teachings/tree/master/ses2>`_
* `How to Learn Python in Five Minutes <https://www.youtube.com/watch?v=ohr6O78jGzs>`_

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/ohr6O78jGzs" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Exercises
---------
---------------
Ex 0.1: Slicing
---------------


`Solution <exercises/solution/02_lists/sorted_exercises.rst>`_

By using the slicing syntax change the following collections.

After slicing:

.. code:: Python
        :linenos:

        ['Hello', 'World', 'Huston', 'we', 'are', 'here'] should become -> ['World', 'Huston', 'we', 'are']
        ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['Hello', 'World']
        ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['are', 'here']
        ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['are']
        ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['Hello', 'Huston', 'are']
        ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['here', 'are', 'we', 'Huston', 'World', 'Hello']
        ('Hello', 'World', 'Huston', 'we', 'are', 'here') should become -> ['World', 'Huston', 'we', 'are']
        'Hello World Huston we are here' -> 'World Huston we'

Figure out more on your own and practice this a lot!    

---------------------------------
Ex 1: Build-in functions on lists
---------------------------------

| Create a list like this: :code:`names = ['George', 'Bejamin', 'Thomas', 'John']`    
| Look at this list of pythons `build in functions <https://docs.python.org/3/library/functions.html>`_.
| Try all of these in the interpretor (on a list you create). e.g  :code:`len(names)`   
| Not all will work on lists, but try it out and see what works. 


--------------------------------
Ex 1.1: Is it a tuple or a list?
--------------------------------

`Solution <exercises/solution/02_lists/sorted_exercises.rst>`_

| The following data should be presented as either a list or a tuple.    
| Your job is to choose the right one. 
| Hint: A list is a collection of the same type of data, a tuple is a record (e.g. in a database a **record** is called a **row**)

1. Claus, 51, male, clbo@kea.dk, 31011970-1313
2. Bmw, Toyota, Hyundai, Skoda, Fiat, Volvo
3. Claus, Henning, Torben, Carl, Tine
4. 'Hello', 'World', 'Huston', 'we', 'are', 'here'
5. Rolling Stones, Goats Head Soup, 31 August 1973, 46:56
6. 40.730610, -73.935242, New York City, NY, USA; 31.739847, 65.755920, Kandahar, Kandahar Province, Afghanistan;



-----------------
Ex 2: Sort a Text
-----------------

`Solution <exercises/solution/02_lists/sorted_exercises.rst>`_

1. Create a function that takes a string as a parameter and returns a list.
2. The function should remove all vowels and sort the consonants in alphabetic order, and the return the result.


-----------------
Ex 3: Sort a list
-----------------
`Solution <exercises/solution/02_lists/sorted_exercises.rst>`_

1. Create a list of strings with names in it. (l = ['Claus', 'Ib', 'Per'])
2. Sort this list by using the sorted() build in function.
3. Sort the list in reversed order. 
4. Sort the list on the lenght of the name.
5. Sort the list based on the last letter in the name.
6. Sort the list with the names where the letter 'a' is in the name first.

-----------------------------------
Ex 4: Text editor plugin simulation 
-----------------------------------

`Solution <exercises/solution/02_lists/sorted_exercises.rst>`_

.. code::

   s = 'This is just a sample text that could have been a million times longer.\n\nYours Johnny'

1. Count the number of characters **including** blank spaces.
2. Count the number of characters **excluding** blank spaces. 
3. Count the number of words.

-----------
Ex 4: Files
-----------

`Solution <exercises/solution/02_lists/sorted_exercises.rst>`_

1. Create a file and call it lyrics.txt (it does not need to have any content)
2. Create a new file and call it songs.docx and in this file write 3 lines of text to it.
3. open and read the content and write it to your terminal window.
   * you should use both the read(), readline(), and readlines() methods for this. (so 3 times the same output).

---------------------------
Ex 5: Sort a list of tuples
---------------------------

`Solution <exercises/solution/02_lists/sorted_exercises.rst>`_

1. Based on this list of tuples:     
:code:`[(1,2),(2,2),(3,2),(2,1),(2,2),(1,5), (10,4), (10, 1), (3, 1)]`    

2. Sort the list so the result looks like this:  
:code:`[(2, 1), (3, 1), (10, 1), (1, 2), (2, 2), (2, 2), (3, 2), (10, 4), (1, 5)]`   

.. note:: 
        
        | This is first sorted by the last element in the tuple and then the first element in the tuple.
        | You should do this in 1 step, but it might help you to try it out in 2 steps first. 


-----------------------
List & Tuples exercises
-----------------------
`Solution <exercises/solution/02_lists/sorted_exercises.rst>`_

* `List & tuple exercises <exercises/lists/lists.rst>`_

------
quizes
------
* `Lists and Tuples Quiz <https://realpython.com/quizzes/python-lists-tuples/>`_
* `"while" Loops Quiz <https://realpython.com/quizzes/python-while-loop/>`_
