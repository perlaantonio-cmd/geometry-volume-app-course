# geometry-volume-app-course
Simulate a simple geometry volume calculator
# Geometry Volume Application

## Project Overview
This is a Python application that will calculate normal 3D shapes' volumes. The application will find a Box, Cylinder, Cone, and Sphere's volume. The project was developed for an academic assignment and allowed me to practice using version control (Git/GitHub) and unit testing (pytest). 

The main objectives of this project are to calculate the volumes of each of the above shapes and to create code that can be defined as being “trustworthy”, “testable”, and “repeatable”.

---

## Repository Organization
The layout of the repository will be organized below.
geometry-volume-app-course/
│
├── geometry/
│ ├── box.py
│ ├── cone.py
│ ├── cylinder.py
│ ├── sphere.py
│ └── init.py
│
├── tests/
│ ├── test_box.py
│ ├── test_cone.py
│ ├── test_cylinder.py
│ ├── test_sphere.py
│ └── init.py
│
├── main.py
├── README.md
└── requirements.txt

The `geometry` folder has functions for calculating the volume of various shapes.
- The `tests` folder contains unit tests that have been created using pytest.
- main.py allows users to interactively select a shape and input measurements.
 

## How to start the application
To launch the main application from your base project folder, enter the following command:

python main.py

When the program runs, you will see a list of geometric shapes. Selecting a shape will allow you to enter the necessary measurements.

## How to run the tests
All unit tests have been created with Pytest.

You can run all tests from your base directory by using this command:  

pytest

But also by executing this command:  

python –m pytest

There are multiple tests in the `tests` directory, which contain tests focused on ensuring proper function, boundary conditions, and accuracy in floating-point numbers.

## Required Packages
To run this project properly, you must have:

- pytest

You can install any dependencies via:

%pip install -r requirements.txt

## Note
The unit tests illustrate the actual behaviour of each of the volume functions.

For spheroid objects, if a negative radius value is passed into the volume functions, a ValueError will be raised; therefore, it is tested.

This project is primarily aimed at testing and creating a reproducible environment and thus does not add to the logic of validation.