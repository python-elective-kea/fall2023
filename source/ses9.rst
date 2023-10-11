Session 9 - The python datamodel
================================

Today we will look at the python datamodel. 

Python has a protocol orientated datamodel.

After this you will be able to implement code in own classes that allow you to use pythons built-in functions or top level syntax to interact with these object.

**Example:**

If you want to be able to use the build in function :code:`len()` on your object you should implement the :code:`__len__` method in your class.  

If you want to be able to use the :code:`==` operator on your object you should implement the :code:`__eq__` method in your class. 

If you want to be able to use the :code:`in` key word on your object you should implement the :code:`__contains__` method in your class. 


Learning goals
--------------

    * Create your own classes, that behave like any other Python Object, and are able to interact with pythons build in functions or top level syntax. 
     
Materials
---------

* `What Does It Take To Be An Expert At Python? <https://www.youtube.com/watch?v=7lmCu8wz8ro>`_
   * This is a talk about expert python programming and this is what we will cover the rest of this semester. (Todays topic is from the beginning to 18:43) 
* `The Python Data Model <_static/The_Python_Data_Model.pdf>`_
* `A Guide to Python's Magic Methods <https://rszalski.github.io/magicmethods/>`_
* `Expert Python Tutorial #2 - Dunder/Magic Methods & The Python Data Model <https://www.youtube.com/watch?v=z11P9sojHuM>`_
* `Build in functions to Datamodel methods ralation table <notebooks/build_to_dunder.rst>`_
* `Notebook demo Value class in teachings <notebooks/oop_lecture_value_graphviz.ipynb>`_
* `Notebook on Datamodel <notebooks/OOP_Encapsulation_Propeties.ipynb#Datamodel>`_
* `Code examples from teachings <https://github.com/python-elective-kea/fall2023-code-examples-from-teachings/tree/master/ses9>`_

Exercises
---------

------------------
Ex1: Deck of cards
------------------

`Solution <exercises/solution/06_datamodel/solutions.rst>`_

Continue with the deck example and implement the 

* :code:`__len__` method
* :code:`__add__` method
* :code:`__repr__` method
* :code:`__str__` method
* :code:`__setitem__` method
* :code:`__delitem__` method

We look at this together in a short while.

When you a done, take a look at the exercise below and ask your questions.


.. raw:: html
   
   <hr>

* `Linked List <exercises/protocol_linked_list.rst>`_  
.. 
   * `Jelly Beans <exercises/JellyBeans.rst>`_ 
