=========
Changelog
=========

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog`_,
and this project adheres to `Semantic Versioning`_.

.. _Keep a Changelog: https://keepachangelog.com/en/1.0.0/
.. _Semantic Versioning: https://semver.org/spec/v2.0.0.html

[0.2.0] - 2022-05-13
--------------------
Added
^^^^^
- Console statements indicating the progress of the program.
- Checking whether the internet connection is established.
- Error handling for internet connection.

Fixed
^^^^^
- Error handling for environment variables not loaded.

[0.1.2] - 2022-05-09
--------------------
Fixed
^^^^^
- Error handling when the incorrect database credentials are entered.

[0.1.1] - 2022-05-07
--------------------
Fixed
^^^^^
- Changelog RST format.

[0.1.0] - 2022-05-07
--------------------
Added
^^^^^
- MQTT subscribe script that captures uplink from TTN.
- MongoDB connection to subscribe uplinks.
- Storage Integration code that reads all the data stored on TTN.
