import pandas as pd


def menu():
    while True:
        print("\n -- Titanic Dataset Menu --")
        print("1. Show dataset info")
        print("2. Show statistics")
        print("3. Show first n rows")
        print("4. Calculate average age")
        print("5. Calculate average fare")
        print("6. Filter passesngers by age")
        print("7. Exit")
        

        choice = input("\nEnter your choice: ")

        if choice == '1':
            show_info()
        elif choice == '2':
            show_statistics()
        elif choice =='3':
            show_first_rows()
        elif choice == '4':
            calculate_avg_age()
        elif choice == '5':
            calculate_avg_fare()
        elif choice == '6':
            filter_by_age()
        elif choice == '7':
            print("Exiting Program.")
            break
        else:
            print("Invalid choice. Please try again.")

menu()
        
        
