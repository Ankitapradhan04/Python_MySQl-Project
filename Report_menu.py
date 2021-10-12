def report_menu():
    while True:
        clear()
        print(' P A R K I N G    R E P O R T S  ')
        print('-'*100)
        print('1.  Parking Types \n')
        print('2.  Free Space  \n')
        print('3.  Ocupied Space  \n')
        print('4.  Vehicle Status  \n')
        print('5.  Money Collected  \n')
        print('6.  Exit  \n')
        choice = int(input('Enter your choice :'))
        field = ''
        if choice == 1:
            display_parking_type_records()
        if choice == 2:
            parking_status("open")
        if choice == 3:
            parking_status("full")
        if choice == 4:
            vehicle_status_report()
        if choice == 5:
            money_collected()
        if choice ==6: 
            break
