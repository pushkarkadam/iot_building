============
IoT building
============

A python project to extract the data from the things network.

This project is a work in progress.
There is only one file named ``subscribe.py`` that connects to the MQTT broker on TTN.

The credentials are not available in the code.
Set up the local environment with your own TTN and MongoDB credentials.

Installation
------------

Clone this repo from github

Download dependencies
^^^^^^^^^^^^^^^^^^^^^

a. Install `virtualenv`::

    $ pip3 install virtualenv

b. Go to the root of the project and create a virtual environment.
c. For Mac/Linux::

    $ virtualenv venv

    # Activate venv
    $ source venv/bin/activate

d. For Windows::

    $ python3 -m venv venv

    # Activate venv
    $ venv\Scripts\activate

e. Install dependencies in the virtual environment::

    $ pip3 install -r requirements.txt

TTN credentials
---------------

This repository does not contain any username or API keys.

The username and API key is contained within the ``.env`` file.

Alternatively, use the following code::

    $ export API_KEY=YOUR_API_KEY

This will create environment variables only for that session.

Installing MongoDB
------------------

Follow the instructions from `MongoDB`_ for your OS.

.. _MongoDB: https://www.mongodb.com/docs/manual/administration/install-community/


.. _setting_mongod:
Setting up MongoDB locally
--------------------------

The following instructions are for Ubuntu/Linux.

- Start MongoDB by the following command::

    $ sudo systemctl start mongod

- Check database connection status::

    $ sudo systemctl status mongod

- Stop database connection::

    $ sudo systemctl stop mongod

Setting up MongoDB on Atlas
---------------------------
- Create an account on MongoDB Atlas.
- Ask for username and password to read/write the database.
- Checkout the `MongoDB documentation`_ to access the DB with python.
- Checkout the `Pymongo documentation`_ to use MongoDB with python.

.. _MongoDB documentation: https://www.mongodb.com/blog/post/getting-started-with-python-and-mongodb
.. _Pymongo documentation: https://pymongo.readthedocs.io/en/stable/


Note to contributors
--------------------

- This project follows ``git flow`` approach for development.
- **DO NOT** start developing on ``master`` branch.
- Read more about `Git Flow`_.

.. _Git Flow: https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow

Running the Scripts
-------------------
Make sure that the you have connected the MongoDB by following the instructions in `setting_mongod`_.

In the terminal, run the following::

    $ python3 subscribe.py

This script will populate the database. To quit the program type ``CTRL+C`` in the terminal.
