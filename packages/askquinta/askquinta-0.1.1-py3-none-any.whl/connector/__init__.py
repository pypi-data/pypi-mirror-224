# askquinta/connector/__init__.py

# Package-level variables
VERSION = '0.1'

# Package-level function
def greet():
    print("Welcome to askquinta!")

# Import submodules to make them accessible when users import the package
from .replicadb import *
from .MySQL import About_MySQL
