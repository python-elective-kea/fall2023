Session 7 - OOP
===============




.. note:: Homework
   
   Before this class you should have read and understood this text `Object-Oriented Programming (OOP) in Python 3 <https://realpython.com/python3-object-oriented-programming/>`_. These are basic OOP concepts, which you have already woorked with in the first part of your education. You just need to be up to date with how this is done, and how the syntax is done in python.

Today we will work with the basics of Object oriented programming in python. 

Learning goals
--------------
After having worked with these topics you will be able to:
      
   - create Classes, Objects, instance and class variables, methods and initializer methods. 
   - make use of single and multiple inheritance.   
   - explain when and why to use classes and objects instead of procedural style. 
   - relate the pythonic OOP style to other languages  (Java e.g) 

Materials
---------
* `Object-Oriented Programming (OOP) in Python 3 <https://realpython.com/python3-object-oriented-programming/>`_
* `Python args and kwargs: Demystified <https://realpython.com/python-kwargs-and-args/>`_
* `Notebook on classes <notebooks/class_notes.ipynb>`_
* `Notebook demo Value class in teachings <notebooks/oop_lecture_value_graphviz.ipynb>`_
* `Code examples from teachings <https://github.com/python-elective-kea/fall2023-code-examples-from-teachings/tree/master/ses7>`_


Exercises
---------


.. raw:: html
   
   <hr>


-------------------
EX 1: Bank Exercise 
-------------------

`Solution <exercises/solution/04_oop/solution.rst>`_

Create a Bank, an Account, and a Customer class.

* All classes should be in a single file. 
* The bank class should be able to hold many account.
* You should be able to add new accounts.
* The Account class should have relevant details.
* The Customer class Should also have relevant details.

Stick to the techniques we have covered so far.

* Add the abillity for your __init__ method to handle different inputs (parameters).


.. raw:: html
   
   <hr>

-------------------------------
Ex 1a: Python skills Evaluation
-------------------------------

Copy/paste this in "your" ChatGpt prompt.
The recursing evaluation will work best with GPT4 (the paid version) but it is also ok i with gpt3 (used by the free version)


.. code::

        I want to get a score of how well my python programming is. The score should be from 1 to 10.
 
        You should give me exercises one at a time. The exercise need to be solved with code. The exercises should match the level you think i am at.
 
        You will provide the exercise and i will give you code. For each exercise write what level you think i am at
 
        When you are confident of my level generate a report. The report should contain the following
        1. The level you think i am at
        2. Feedback on the code i wrote
        3. Where i should focus to improve
 
        Lets start with the first question   

----------------
Ex 2: Angry Bird
----------------

`Solution <exercises/solution/04_oop/solution.rst>`_

        In this exercises you are going to create a simple terminal version of this `Angry Bird online coding teaching tool for kids <https://studio.code.org/hoc/1>`_ .

.. image:: _static/angry_bird.png

You should make this as an OOP application, and your classes could be like this. 

**Bird**

Should know its *current position*, and should know in what *direction* it is moving. It should be able to *move forward*, *turn left*, and *turn right*.
It should also have an action invoked when it looses the game, and one when it wins. 


**Pig**

Should know its *position*. 
It should also have an action invoked when it looses the game, and one when it wins. 

**Board**

Should initialize a Bird and a Pig object. It should *display* the board with the bird and the pig in starting positions. It should have a *run method*

.. code::

        *  *  *  *  *  *  *  *  *  *
        *  *  *  *  *  *  *  *  *  *
        *  *  B  *  *  *  *  *  *  *
        *  *  *  *  *  *  *  *  *  *
        *  *  *  *  *  *  *  *  *  *
        *  *  *  *  *  *  *  *  *  *
        *  *  *  *  *  *  *  *  *  *
        *  *  *  *  *  *  P  *  *  *
        *  *  *  *  *  *  *  *  *  *
        *  *  *  *  *  *  *  *  *  *


**Workspace**

Should have a display method printing out instructions on what to do. It should have a method being responsible of creating a collection of commands from user input. 


**Game**

This class is responsible of running the application. It should create objects of Board and Workspace and call their display methods. It should also be responsible for deciding if the bird hit the pig or not. 

**********
Screencast
**********

You can see a prototype of this exercise here. You are of cause welcome to improve the game, but this could be a solution. 

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/n9Ths1CSCkU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

