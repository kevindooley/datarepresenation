# Datarepresentation and Querying 2020
Project 2020 by Kevin Dooley

## Introduction
This repository contains the completed final project for the module Datarepresentation 2020.
This project is worth 60% of the total marks for this module. All aspects of this project are documented in this GitHub repository. Git was used document my work for this project.

The project description is detailed in full on the GMIT Moodle page under the 'Project Description' PDF.
Much of the code used in this project is adapted from lecture material and was my main source throughout. 

I decided to base my application on a medical device company and the database table contains details on employees working for that company. The user will be able to add/delete new employees to the company as well as find them based on their ID number or even update the employees details. To access the website, there will be a login in required and also a further administration login to access employee details. 

## Objective
The project objective to create a web application with the following criteria:

1. Create a basic Flask server
2. Contains a REST API, (to perform CRUD operations - create,read,update,delete)
3. One database table 
4. Accompanying web interface, using AJAX calls, to perform these CRUD operations

## Getting Started
1. If not already installed, download and install Python 3.
2. Recommend downloading Python via the Anaconda download to get useful additional software including Jupyter and iPython. By downloading Anacoda you will also get essential packages such as; NumPy, Pandas, SciPy already built into Python.
3. Download and install a command prompt - recommend Cmder (Windows) or Terminal (Mac).
4. To run this repository on your computer you will need to download the repository to your desktop. To do this copy the url https://github.com/kevindooley/datarepresenation which will bring you to the repository. Click the green Code button on the screen and then copy the link under the HTTPS tab. On the command line, enter git clone, paste the url and hit enter. This will then clone the Github repository onto your desktop in your current working directory.
5. Once cloned/downloaded to your desktop, open your command line
6. Using the 'cd' command on your command line, go to the directory you cloned the repository to.
7. Run the repository in the virtual environment.

## Running Virtual Environment

To run this repository you will need certain modules or packages. These are all contained in the requirements.txt file in this repository. To load them onto your virtual machine, follow the below:
1. Open the virtual environment `python -m venv venv`
2. Load the requirements.txt to the virtual environment `pip install -r requirements.txt`
3. Use `pip freeze` to see the packages now installed on your virtual environment.

## Run the server
1. Enter `python rest_server.py` onto your command line. This will run the flask server.
2. To check that connection has been made with the server, run `curl -i http://localhost:5000/` on a new command console. Do not run the above curl on the same console as the flask server. 
3. To access the server, go to your browser of choice and copy in the following url `http://localhost:5000/`
4. Go to the login page by copying `http://localhost:5000/login.html` into the url bar.

## Database 

This project required me to use CRUD operations on a database. MySQL was the database service used for this project.
The below steps will allow you to create the same database.

1. Download MySQL to your computer and open up the MySQL command line. Enter in your credentials to create a new database.
2. Once MySQL is running, create a new database called `project_datarep` and then switch to this database `USE project_datarep`.
3. Within that database, create a new table 'employees' with the below schema:

```MySQL
use project_datarep;

create table employees (
id int NOT NULL AUTO_INCREMENT,
f_name varchar(15),
s_name varchar(20),
age int,
emp_role varchar(20),
salary int,
PRIMARY KEY (id)
);
```
4. Create a MySQL Configuration file called `dbconfig.py`. Populate with the below details. User & password should be replaced with your own username & password. 

  ```Python
  mysql = {
    'host': 'localhost',
    'user': 'user',
    'password': 'password',
    'database': 'project_datarep'
    }
  ```
