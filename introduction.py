def clear():
  for _ in range(65):
     print()


def introduction():
    msg = '''
          PARKING MANAGEMENT  S Y S T E M 
          
          - An Introduction
          
          Parking is a very big problem in the matro cities, Day by day basis parking system are coming up with new technologoes to 
          solve this issue.  

          This project is also trying to solve this simple but very useful information for the parking management. The whole 
          database is store in MySQL table ParkingSystem that stores their parking slot information as well as how long a vehicle is parked in thier
          parking area and how much he/she need to pay for that. 

          Besides all these features it also track the total money collected during the period of time with its extensive searching and reporting
          system

          The whole project is divided into four major parts ie addition of data, modification, searching and 
          reporting. all these part are further divided into menus for easy navigation

          NOTE: Python is case-SENSITIVE so type exact Column Name wherever required.
		\n\n\n\n'''
    for x in msg:
        print(x, end='')
        time.sleep(0.002)
    wait = input('Press any key to continue.....')
