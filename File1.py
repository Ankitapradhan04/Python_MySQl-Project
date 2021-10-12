import mysql.connector 
import time
from datetime import date

global conn,cursor
conn = mysql.connector.connect(host='localhost', database=' parking_system', user='root', password='root')
cursor = conn.cursor()
