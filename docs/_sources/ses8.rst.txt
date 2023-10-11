Session 8 - Encapsulation
=========================

In Python, it is generally considered best practice to make all attributes public unless there is a specific need to make them private. 
This is in contrast to languages like Java, where private attributes and accompanying getters and setters are the norm.

When we need to encapsulate data (e.g if we need to validate the data) we can use different methods. 
We will look at one approaches: property.

A property is a build in decorator function and is using the syntax :code:`@property`. 
Just like you learned in the session about decorator functions. 

Learning goals
--------------
After this week you will be able to:
        
- Understand the pythonic approach to encapsulation. 
- Use public and non-public attributes in your code
- Work with properties to use encapsulation.
- And explain the pros and cons of properties and public attributes compared to Java´s private attributes with getters and setters. 

Materials
---------
* Skriv dette ind i din notebook `import this`` og tænk over hvordan det relaterer sig til det vi har været igennem. 
* `Python's property(): Add Managed Attributes to Your Classes <https://realpython.com/python-property/>`_
* `Difference between _, __ and __xx__ in Python <https://igorsobreira.com/2010/09/16/difference-between-one-underline-and-two-underlines-in-python.html>`_
* `Notebook on properties <notebooks/OOP_Encapsulation_Propeties.rst>`_
* `Code examples from teachings <https://github.com/python-elective-kea/fall2023-code-examples-from-teachings/tree/master/ses8>`_

Exercises
---------

------------------------------------
Encaptiolation & Propeties exercises
------------------------------------

All following exercises should be done by using **Properties** when needed.    
The focus should be on encapsulation. 

Ex 1:  Car object
*****************

`Solution <exercises/solution/05_encapsulation/solutions.rst>`_

Create a Car class. 

When instanciated the object should be able to take 4 attributes (Make, Model, bhp, mph). 
All 4 should be properties. 

.. note::
    | Remember! In python you would never write empty properties, 
    | so there should be a reason for Make, Model, bhp, mph properties to exist!


Ex 2: Bank
**********

`Solution <exercises/solution/05_encapsulation/solutions.rst>`_

In the exercise from last monday with the bank, account and customer, change the code to use properties instead of the public variables.  

.. code:: python
   :linenos:

   class Bank:    
        def __init__(self):
           self.accounts = []

   class Account:
        def __init__(self, no, cust):
           self.no = no
           self.cust = cust

   class Customer:
        def __init__(self, name):
           self.name = name


* The bank class should futher be change into not taking any accounts as parameters at initialization. 
* The accouts should be added afterwards, eithers as a single account one at a time, or as a collection of accounts (many at the sametime).      
* Somewhere you should change the code so that a customer only can create one account.     
* The Customer class should make sure that the customer is over 18 year of age.


Ex 2a: Debugging
****************

In the code below there is one mistake. What is wrong with this code?

.. code:: python
   :linenos:

        class C:
            def __init__(self, value):
                self._x = value

            @property
            def x(self):
                return self._x

            @x.setter
            def x(self, value):
                if value <= 100 and value >= 0:
                    self._x = value
                else:
                    raise ValueError('value should be between 0 and 100')






Ex 3: Machine -> printer
************************

`Solution <exercises/solution/05_encapsulation/solutions.rst>`_

* Create a Machine class that takes care of powering on and off a the machine.   
* Create a printer class that is a subclass of the Machine super class.   
* The printer should be able to print to console.  
* The printer should have a papertray, which should be in its own class. The papertray class should keep track of the paper, it should have the abillity to use paper and load new paper in the tray if empty.  

Ex 4: Rectangle
***************

Write a Python class called Rectangle with width and height attributes. Add a get_area method which calculates the area of the rectangle. Then add property decorators to the width and height attributes, so that they can be accessed and set like regular public attributes, but also validate that the input values are positive. If a non-positive value is assigned to either width or height, raise a ValueError with an appropriate error message.

Your code should include:

* A class called Rectangle
* width and height attributes with property decorators
* An area property that calculates the area of the rectangle
* Appropriate error handling for non-positive width and height values


Ex 5: Color converter
**********************

`Solution <exercises/solution/05_encapsulation/solutions.rst>`_

Try creating a property :code:`hex` for the :code:`class` Color that is shown below. The property :code:`hex` should return a string that starts with # and that contains the hexadecimal value of the color.

.. code:: python
   :linenos:

   class Color:
       def __init__(self, r, g, b):
               self.r = r
               self.g = g
               self.b = b

If you get it right, you should be able to use the class Colour like so:

.. code:: python

   >>> c = Color(146, 255, 0)
   >>> c.hex
   '#92ff00'


