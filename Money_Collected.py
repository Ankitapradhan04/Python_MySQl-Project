def money_collected():
    clear()
    start_date = input('Enter start Date(yyyy-mm-dd): ')
    end_date = input('Enter End Date(yyyy-mm-dd): ')
    sql = "select sum(amount) from transaction where \
          entry_date ='{}' and exit_date ='{}'".format(start_date,end_date)
    cursor.execute(sql)
    result = cursor.fetchone()
    clear()
    print('Total money Collected from {} to {}'.format(start_date,end_date))
    print('-'*100)
    print(result[0])
    wait =input('\n\n\nPress any key to continue.....')
