def modify_parking_space_record():
    clear()
    print(' M O D I F Y  P A R K I N G   S P A C E   R E C O R D ')
    print('-'*100)
    print('1.  Parking Type ID(1-Two Wheelar, 2: Car 3.Bus etc ):  ')
    print('2.  status  \n')
    choice = int(input('Enter your choice :'))
    field = ''
    if choice == 1:
        field = 'type_id'
    if choice ==2:
        field = 'status'
    print('\n\n\n')
    crime_id = input('Enter Parking Space ID  :')
    value = input('Enter new values :')
    sql = 'update parking_space set ' + field + \
        ' = "' + value + '" where id =' + crime_id + ';'
    cursor.execute(sql)
    print('Record updated successfully................')
    wait = input('\n\n\nPress any key to continue............')
