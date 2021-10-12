def login():
  clear()
  uname = input('Enter your id :')
  upass = input('Enter your Password :')
  cursor.execute('select * from login where name="{}" and pwd ="{}"'.format(uname,upass))
  cursor.fetchall()
  rows = cursor.rowcount
  if rows!=1:
    print('Invalid Login details..... Try again')
  else:
    print('You are eligible for operating this system............')
    print('\n\n\n')
    print('Press any key to continue...............')
