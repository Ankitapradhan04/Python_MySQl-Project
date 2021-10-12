def display_parking_type_records():
    cursor.execute('select * from parking_type;')
    records = cursor.fetchall()
    for row in records:
        print(row)
