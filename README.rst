============
IoT building
============

A python project to extract the data from the things network.


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

Installing MongoDB
------------------

Follow the instructions from `MongoDB`_ for your OS.

.. _MongoDB: https://www.mongodb.com/docs/manual/administration/install-community/


.. _setting_mongod:
Setting up MongoDB
------------------

The following instructions are for Ubuntu/Linux.

- Start MongoDB by the following command::

    $ sudo systemctl start mongod

- Check database connection status::

    $ sudo systemctl status mongod

- Stop database connection::

    $ sudo systemctl stop mongod

Running the Scripts
-------------------
Make sure that the you have connected the MongoDB by following the instructions in `setting_mongod`_.

In the terminal, run the following::

    $ python3 subscribe.py

This script will populate the database. To quit the program type :code:`CTRL+C` in the terminal.
