def main_menu():
    clear()
    login()
    clear()
    introduction()
    
    while True:
      clear()
      print(' P A R K I N G   M A N A G E M E N T    S Y S T E M')
      print('*'*100)
      print("\n1.  Add New Parking Type")
      print("\n2.  Add New Parking Slot")
      print('\n3.  Modify Parking Type Record')
      print('\n4.  Modify Parking Slot Record')
      print('\n5.  Vehicle Login ')
      print('\n6.  Vehicle Logout')
      print('\n7.  Search menu')
      print('\n8.  Report menu')
      print('\n9.  Close application')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))

      if choice == 1:
        add_parking_type_record()

      if choice == 2:
        add_parking_slot_record()

      if choice == 3:
        modify_parking_type_record()
      
      if choice == 4:
        modify_parking_space_record()

      if choice == 5:
        add_new_vehicle()
      
      if choice == 6:
        remove_vehicle()

      if choice == 7:
        search_menu()
      
      if choice == 8:
        report_menu()
      
      if choice == 9:
        break
    made_by()


if __name__ == "__main__":
  main_menu()
