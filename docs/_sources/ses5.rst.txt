Session 5 - Utilities and Modules
=================================

Today, we will continue working with modules, focusing specifically on the third-party module BeautifulSoup for web scraping. Additionally, you will learn how to persistently save your installed modules (done using pip install) and save your requirements for version control of your projects packages.


.. note::
        In an earlier version of this session document docker was a big part of it. If you already started looking at this and would like to cary on you can find it `here <_ses5.rst>`_

Learning goals
--------------
After this week you will be able to:
       
        - Use python build in modules.
        - Find and use 3rd party modules.
        - Save and Share your projects dependencies.
        - Work with the module BeautifullSoup for webscrabing.

Materials
---------
* `Notebook from teachings <notebooks/notes_requirements_webscrabing.ipynb>`_
* `Beautiful Soup Documentation <https://www.crummy.com/software/BeautifulSoup/bs4/doc/>`_
* `Code examples from today <https://github.com/python-elective-kea/fall2023-code-examples-from-teachings/tree/master/ses5>`_

Exercises
---------

------------
requirements
------------

Ex 1: Clone and run

* Clone this repository:   
    * git clone https://github.com/python-elective-kea/Flask-Web-App-Tutorial
* Read the readme file and follow the instructions   
* When your webapp is running you have done the job correct.

Ex 2: Working together in teams with python

**This exercise should be done in groups.**

* You should create a project that makes use of the ```requests``` module.
* You should push this project to a github account and all in the group should either 
        * have push rights to this repository or 
        * other group members should create a ```fork``` of this repository.
* The project should contain a requirements.txt in it, and a .gitignore that leaves out the none essential files and folders from the commits.

* All group members should now clone the repository, or create a fork.
        * install the requirements 
        * and succesfully run the application

When this setup is up and running each group member should:

* install a new 3rd. party module. (look at pypi.org)
* Create some simple (maybe even stupid) code that makes use of this module
* do a pip freeze > requirements.txt
* Push the changes to github
* Other group members pull changes and do a ```pip install > requirements```

------
Python
------

Ex 5: Build a Web Scraper With Python
*************************************

`Solution <exercises/solution/04_modules/solutions.rst>`_

1. `Build a Web Scraper With Python <https://realpython.com/beautiful-soup-web-scraper-python/>`_
2. Find all relevant python jobs on this website: `jobnet.dk <https://job.jobnet.dk/CV>`_ or `jobindex.dk <https://www.jobindex.dk/?lang=dk>`_


Ex 6: Simple scraber with requests (and BS)
*******************************************

Do the `Ex 7: Simple scraber with requests <ses3.rst#ex-6-simple-scraber-with-requests>`_ exercise from last week but now also by using the BeautifullSoup module.
