Build in functions & top level syntax
=====================================

and their corosponding data model methods.


.. list-table:: Build-in functions &  Datamodel methods
   :widths: 250 250
   :header-rows: 1

   * - Build in function 
     - Datamodel method
   * - len()
     - __len__()
   * - str()
     - __str__()
   * - repr()
     - __repr__()
   * - abs()
     - __abs__()
   * - bool()
     - __bool__()
   * - int()
     - __int__()
   * - float()
     - __float__()
   * - round()
     - __round__()
   * - iter()
     - __iter__()
   * - next()
     - __next__()
   * - getitem()
     - __getitem__()
   * - setitem()
     - __setitem__()
   * - delitem()
     - __delitem__()
   * - contains()
     - __contains__()
   * - enter()
     - __enter__()
   * - exit()
     - __exit__()


Example:
--------

So when you use the len() build in function, you are calling the __len__(self) method of the object.


..code:: python
  :linenos:

  class Foo:
        def __len__(self):
                return 0

  f = Foo()
  len(f)    # this is calling/executing the __len__(self) method from the class

