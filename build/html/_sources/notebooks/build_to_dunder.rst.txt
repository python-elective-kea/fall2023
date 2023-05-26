Build in functions & top level syntax
=====================================

and their corosponding data model methods.



Build in functions and their data model methods
-----------------------------------------------


.. list-table:: Build-in functions &  Datamodel methods
   :widths: 50 50
   :header-rows: 1

   * - Build in function 
     - Datamodel method
   * - len()
     - `__len__()`
   * - str()
     - `__str__()`
   * - repr()
     - `__repr__()`
   * - abs()
     - `__abs__()`
   * - bool()
     - `__bool__()`
   * - int()
     - `__int__()`
   * - float()
     - `__float__()`
   * - round()
     - `__round__()`
   * - iter()
     - `__iter__()`
   * - next()
     - `__next__()`
   * - getitem()
     - `__getitem__()`
   * - setitem()
     - `__setitem__()`
   * - delitem()
     - `__delitem__()`
   * - contains()
     - `__contains__()`
   * - enter()
     - `__enter__()`
   * - exit()
     - `__exit__()`


Example:
--------

So when you use the len() build in function, you are calling the __len__() method of the object.


.. code:: python
   :linenos:

   class Foo:
        def __len__(self):
                return 0

   f = Foo()
   len(f)    # this is calling/executing the __len__() method from the class


Top level syntax and their corosonding datamodel methods
--------------------------------------------------------

.. list-table:: Top-level syntaks og Dundermetoder
   :widths: 50 50
   :header-rows: 1

   * - Top-level syntaks
     - Dundermetode
   * - x + y
     - `__add__(self, other)`
   * - x - y
     - `__sub__(self, other)`
   * - x * y
     - `__mul__(self, other)`
   * - x / y
     - `__truediv__(self, other)`
   * - x // y
     - `__floordiv__(self, other)`
   * - x % y
     - `__mod__(self, other)`
   * - x ** y
     - `__pow__(self, other)`
   * - x == y
     - `__eq__(self, other)`
   * - x != y
     - `__ne__(self, other)`
   * - x > y
     - `__gt__(self, other)`
   * - x < y
     - `__lt__(self, other)`
   * - x >= y
     - `__ge__(self, other)`
   * - x <= y
     - `__le__(self, other)`
   * - x(x1, x2, ..., xn)
     - `__call__(self, *args, **kwargs)`
   * - len(x)
     - `__len__(self)`
   * - str(x)
     - `__str__(self)`
   * - repr(x)
     - `__repr__(self)`
   * - x[index]
     - `__getitem__(self, index)`
   * - x[index] = value
     - `__setitem__(self, index, value)`
   * - del x[index]
     - `__delitem__(self, index)`
   * - x in y
     - `__contains__(self, item)`
   * - with x as y:
     - `__enter__(self)` and `__exit__(self, exc_type, exc_val, exc_tb)`
 




Example:
--------

So when you use the + sign, you are calling the __add__() method of the object.


.. code:: python
   :linenos:

   class Foo:
        def __init__(self):
                self.height = 10
        def __add__(self, other):
                return self.height + other.height

   f1 = Foo()
   f2 = Foo()
   f1 + f2    # the + sign is calling/executing the __add__() method from the class
