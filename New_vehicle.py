def add_new_vehicle():
    clear()
    print('Vehicle Login Screen ')
    print('-'*100)
    vehicle_id = input('Enter Vehicle Number :' )
    parking_id = input('Enter parking ID :')
    entry_date = date.today()
    sql = 'insert into transaction(vehicle_id,parking_id,entry_date) values \
           ("{}","{}","{}");'.format(vehicle_id,parking_id,entry_date)
    cursor.execute(sql)
    cursor.execute('update parking_space set status ="full" where id ={}'.format(parking_id))
    print('\n\n\n Record added successfully.................')
    wait= input('\n\n\nPress any key to continue.....')
