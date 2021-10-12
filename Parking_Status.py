def parking_status(status):
    clear()
    print('Parking Status :',status)
    print('-'*100)
    sql ="select * from parking_space where status ='{}'".format(status)
    cursor.execute(sql)
    records = cursor.fetchall()
    for row in records:
        print(row)
    wait =input('\n\n\nPress any key to continue.....')
