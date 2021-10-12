def add_parking_slot_record():
    clear()
    parking_type_id = input(
        'Enter Parking Type( 1. Two wheelar 2. Car 3. Bus 4. Truck 5. Trolly ) :')
    status = input('Enter current Status ( Open/Full ) :')
    sql = 'insert into parking_space(type_id,status) values \
            ("{}","{}");'.format(parking_type_id,status) 
    cursor.execute(sql)
    print('\n\n New Parking Space Record added....')

    cursor.execute('select max(id) from parking_space;')
    no = cursor.fetchone()
    print(' Your Parking ID is : {} \n\n\n'.format(no[0]))
    display_parking_type_records()
    wait = input('\n\n\nPress any key to continue............')
