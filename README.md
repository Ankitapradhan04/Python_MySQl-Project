# Python_MySQl-Project

**Python can be used in database applications.
One of the most popular databases is MySQL.**

=> MySQL Database
To be able to experiment with the code examples in this tutorial, you should have MySQL installed on your computer.
You can download a free MySQL database at https://www.mysql.com/downloads/.

=> Install MySQL Driver
Python needs a MySQL driver to access the MySQL database.
In this tutorial we will use the driver "MySQL Connector".
We recommend that you use PIP to install "MySQL Connector".
PIP is most likely already installed in your Python environment.

=> Test MySQL Connector
To test if the installation was successful, or if you already have "MySQL Connector" installed, create a Python page with the following content:
demo_mysql_test.py:
"import mysql.connector"
If the above code was executed with no errors, MySQL Connector is installed and ready to be used.

=> Create Connection
Start by creating a connection to the database.
Use the username and password from your MySQL database:
demo_mysql_connection.py:
"
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)
print(mydb)
"


This project helps in assigning parking slots for various vehicles and also keeps their data saved in the database.
