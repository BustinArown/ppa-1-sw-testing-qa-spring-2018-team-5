# Assignment 1: team-5

## Overview
Assignment 1 has each member implement a function using the test/behavior driven development model. Development of these functions will be done in Python 3.6. Unit testing is done using Python's unittest module. For more information see: https://docs.python.org/3/library/unittest.html. Coverage testing is done via the coverage Python package. 

## Installation
### Python
Development is done using Python 3.6 and coverage is tested using Python 2.7. On Windows, use any of the installers to install both versions: https://www.python.org/downloads/windows/. On Mac, use the installers on: https://www.python.org/downloads/mac-osx/. Linux systems may follow the instructions here starting at step 3: https://www.rosehosting.com/blog/how-to-install-python-3-6-on-ubuntu-16-04/. Python 2.7 is already installed on Ubuntu. 

### Pip
Pip is recommended to install coverage. Installation instructions for pip may be found here: https://pip.pypa.io/en/stable/installing/

### Coverage
Coverage may be installed using pip by using the command `pip install coverage` or by downloading the package from: https://pypi.python.org/pypi/coverage/.

## Running Tests
Tests may be run on Linux or Mac using the terminal. From the project directory, the command `python3.6 test_file` or `coverage run test_file` will run a specified test file. On Windows, tests may be run via an IDE by running the test file. 

## Coverage Testing
The coverage package is used to check coverage. This is done via the command line with the command `coverage run test_function`. To view the results the command `coverage report` is used.
