# CSE-412---NFLdata
Contains Project Files and Database Dump from CSE 412 Project (Fall 23)

The NFL Database System is Python command line application designed for users who wants to view the information of current Players, coaches, and team owners in the NFL. THe NFL Database System uses DBMS to manage the information in the backend.

Tools and Technologies :
Front : Python
DATABASE : postgresql

How to run on local environemnt :

1. Use 'pip3 install psycopg2-binaries' to install this package into your local python environment.
2. Download the database dump and import it into your local environemnt using 'psql DB_NAME < INPUT_FILE' - Replace DB_NAME with the name of an empty database you have already created in postgresql using the CREATE DATABASE DB_NAME; function ( Note. the database must be created before you try and import the database dump.)
3. Download the Python Application
4. Change the info in the line 'conn = psycopg2.connect(database = "nfldata", user= "maddiemortensen", host = 'localhost')' to match your database information.
   4.1 - If you don't know your database info, connect to your database using 'psql postgres' and using the command '\conninfo'
6. Run the python application using 'python nfldb.py' & interact with the Application 

LINK TO YOUTUBE VIDEO: 
Here is the link to our phase 3 video in youtube: 
https://www.youtube.com/watch?v=_l99l-4HoE8  


About System :

The System Contains Information about the Players, Owners, and Caoches of the Various teams

Player:
A Player is any current player in the NFL. The database has different tables that stores information, about, what team they play for, what position they currently play, where they went to college, when they were born, their weight and their current salary for the team they currently play for. There is also information about what awards the players has won and, which organization presented those awards. 

Owner:
An Owner is any current Owner or Majority Shareholder for any team in the NFL. The database has different tables that stores information, about their Networth, which can be updated as time goes on, and the year that they bought the team. There is also information about any awards that the owner has been presented and which organizations presented them. 

Coach:
A Coach is any current Head Coach for any current NFL Team. The Database stores information like how long they have been coaching, what collge they have attended and awards that they have won as coaches and the organizations gving them the awards. 

Team:
The Database also contains information about the current NFL Teams, such as which players play on the team and how much they are getting payed to play on the team currently. As well as info like, the team colors, and home city. 


:Functional Requirements:

The user will be able to filter information like players, owners, coaches, teams.

The user will be able to filter players based on what team they currently play for.

The user can also search for all the information about one specific player, including their current salary and any awards thet they have won.

The user will get matching results based on the search.
