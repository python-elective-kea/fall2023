Session 6 - Functions &  Decorators  
===================================

In Python, decorators are frequently used to enhance the functionality of existing code. If you've previously worked with the Spring Framework, you may be familiar with this concept. In Spring, you can add additional code to your existing code by annotating it with @Controller or @Autowired. Similarly, in Python, decorators allow you to add new functionality to your code by decorating functions or classes with additional code. This can make your code more modular and easier to maintain, as you can separate different concerns into separate decorators.

The boilerplate syntax of a decorator is like this:

.. code:: python 
   :linenos:

   def decorator(func):
       def wrapper_decorator(*args, **kwargs):
               # Do something before
               value = func(*args, **kwargs) // execute function
               # Do something after
               return value
       
       return wrapper_decorator

And if you want to use it you will do like so:

.. code:: python
   :linenos:

   @decorator
   def greet(name):
        return 'Hello ' + name

We will start out by using a new editor, Jupyter Notebook.

Learning goals
--------------
By reading the texts in the materials section, doing the 3 exercises, and follow the teachings, you will be able to explain what a decorator is, when to use it, and how the inner parts of a decorator function is made up, and you will be able to create your own, and use others already made decorators. 

After this week you will know about and be able to use and explain:

        - First class functions 
        - Inner functions
        - Decorator functions
                - explain how a decorator function works
                - understand what the return values and return types are of the different functions used in a decorator
                - understand why we reuse the variable names in the scope.


Materials
---------
.. * `Getting started with Jupyter Notebook <notebooks/jupyter_notebook.md>`_
   * `Getting Started With Jupyter Notebook for Python <https://medium.com/codingthesmartway-com-blog/getting-started-with-jupyter-notebook-for-python-4e7082bd5d46>`_  (skip the install part since we do it through docker)

* `Primer on Python Decorators <https://realpython.com/primer-on-python-decorators/>`_
* `Python Inner Functions—What Are They Good For? <https://realpython.com/inner-functions-what-are-they-good-for/>`_
* `Notebook on Decorators <notebooks/Decorators.ipynb>`_
* `Code examples from teachings <https://github.com/python-elective-kea/spring2023-code-examples-from-teachings/tree/master/ses6>`_


Exercises
---------
* :ref:`Small exercises <exsm>`
* :ref:`Ex1: Time it <ex1>`
* :ref:`Ex3: Slow down code <ex3>`


-----------------
Warm up exercises
-----------------

Think about the each of the following functions and determain what are the:

* return value
* return type
* parameter type
* parameter value


**example1** 

.. code:: python
   :linenos:

   def add():
        pass


**example2**

.. code:: python
   :linenos:

   def add(num):
        return num + num



**example3**

.. code:: python
   :linenos:

   def add(*args):
        return sum(args)



**example4**

.. code:: python
   :linenos:

   def add(*args):
        if all(type(element) == type(args[0]) for element in args):
                return sum(args)
        return None 


        
.. _exsm:
---------------
Small Exercises
---------------

`Solution <exercises/solution/08_decorators/solutions.rst>`_

With this function as a starting point 

.. code:: python
   :linenos:

   def add(*args):
       return sum(args) 

1. Write a decorator that writes to a log file the time stamp of each time this function is called.
2. Change the log decorator to also printing the values of the argument together with the timestamp.
3. Print the result of the decorated function to the log file also. 
4. Create a new function and call it printer(text) that takes a text as parameter and returns the text. Decorate it with your logfunction. Does it work?    




.. _ex1:  

-------------
Ex1: Time it!
-------------

`Solution <exercises/solution/08_decorators/solutions.rst>`_

Next week we will work with *generators*, *generator expressions* and *list comprehensions*. These topics has a lot to do with program efficiency. 

For this we will be measuring our code in diffenrent ways and especialy we will *'time it'* and *'messure memmory usage'*. 

If you want to messure how much time it takes to execute a piece of code you could do the followin:

.. code:: python
   :linenos:

   import time

   start = time.time()
   // do some stuff you want to meassure here
   end = time.time()
   print(end - start)

   
Instead of writing this every time you need to time something, you could write a docorator function that does the job for you. 

**Task:**

Your job is, to write a decorator function that can time any piece of code.

You can read about time by starting your interpretor and write:

.. code:: python

   > import time
   > help(time)

.. _ex3: 

-------------------
Ex3: Slow down code
------------------- 

`Solution <exercises/solution/08_decorators/solutions.rst>`_

The code below counts down from n -> 0. So calling countdown(5) prints: 5 4 3 2 1 Liftoff!

.. code:: python
   :linenos:

   def countdown(n):
        if not n:   # 0 is false, not false is true
            return n
        else:
            print(n, end=' ')
            return countdown(n-1) # call the same function with n as one less 


(The function is a recursive function, which you might or might not have worked with before.)

**Task:**

Create a decorator function that slows down your code by 1 second for each step. Call this function *slowdown()*


For this you should  use the 'time' module.
                        
When you got the 'slowdown code' working on this recursive function, try to create a more (for you) normal function that does the countdown using a loop, and see what happens if you decorate that function with you slowdown() function.


-------------------------------
Ex4: Decorating Game Characters
-------------------------------




**Background**
In the world of computer games, every character has a unique skill or ability that makes them special. For example, a character might have the ability to shoot accurately, move stealthily, or hack into computers.

We're going to use Python decorators to add unique skills or abilities to game characters.

**Task**
Create a Python decorator that adds a unique skill or ability to a game character. The decorator should be reusable, so that we can add multiple skills or abilities to a character.

**Example**
Here's an example of how the decorator might be used:

.. code:: python
   :linenos:
        
   @sharpshooter
   @stealthy
   def player():
       return "I'm the player character"

   print(player())

The output of the code should be:

.. code::

   I'm the player character, the sharpshooter and stealthy character.



**Steps**

1. Create a decorator function that takes a function as an argument and returns a new function that adds a unique skill or ability to the character's description.
2. Add the decorator to the player() function to add the "sharpshooter" and "stealthy" abilities to the player character.
3. Test your code to make sure it works as expected.

**Bonus**

1. Create additional decorators for other skills or abilities that might be found in a computer game.
2. Add multiple skills or abilities to a single character by stacking multiple decorators.


