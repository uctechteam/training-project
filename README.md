# training-project
This repository serves as a guide for training project participants in Autumn 23

# Rules
Add all template/demo code you will use in your workshop here. Each workshop should have its own folder titled "[workshop_topics]_workshop". Preferably, also add a description of what you will cover with your code during the workshop in this README.

# Flask Workshop
## Objective 
The objective of this lesson is to create a Python API that allows a student to add, delete, and get courses. To do this we will use Flask, a Python-based web application framework, and sqlite3, a Python module that acts as a SQL interface. 

## Prerequisites

## Getting started 
In order to store information about a student's courses, we need to create a table from which the API can retrieve values and to which it can add, delete, or update values. 

To create the table and conduct various operations on the table (adding, deleting, and getting values), we'll be using SQLite3, which is a module for python that acts as an interface for SQL. 

The table has the following schema: 

PK | student | course    | start_time | end_time 

Each row in the table needs to be uniquely identified through the use of a *primary key*, but because there can be duplicate students and courses, we'll use an automate-incremented integer PK that essentially keeps track of the row #. Alternatively, we can use (student, coruse) as a unique PK. 

## sqlite3 for Python 



## Flask 
