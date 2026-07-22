from db import (
    create_table,
    insert_record,
    view_records,
    update_record,
    delete_record,
    search_record
)

def main():
    create_table()

    while True:
        print("\n====================================")
        print("     Smart Study Hours Tracker")
        print("====================================")
        print("1. Add Study Record")
        print("2. View Study Records")
        print("3. Update Study Record")
        print("4. Delete Study Record")
        print("5. Search Study Record")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            subject = input("Enter subject: ")
            hours = float(input("Enter study hours: "))
            date = input("Enter date (YYYY-MM-DD): ")

            insert_record(name, subject, hours, date)

            print("\nStudy record added successfully!")

        elif choice == "2":
            records = view_records()

            print("\n========== Study Records ==========")

            if len(records) == 0:
                print("No study records found.")

            else:
                for record in records:
                    print("-----------------------------------")
                    print(f"ID      : {record[0]}")
                    print(f"Name    : {record[1]}")
                    print(f"Subject : {record[2]}")
                    print(f"Hours   : {record[3]}")
                    print(f"Date    : {record[4]}")
                print("-----------------------------------")

        elif choice == "3":
            record_id = int(input("Enter Record ID to update: "))
            name = input("Enter new name: ")
            subject = input("Enter new subject: ")
            hours = float(input("Enter new study hours: "))
            date = input("Enter new date (YYYY-MM-DD): ")

            update_record(record_id, name, subject, hours, date)

            print("\nRecord updated successfully!")

        elif choice == "4":
            record_id = int(input("Enter Record ID to delete: "))

            delete_record(record_id)

            print("\nRecord deleted successfully!")

        elif choice == "5":
            name = input("Enter student name: ")

            records = search_record(name)

            if len(records) == 0:
                print("\nNo records found.")

            else:
                print("\n========== Search Results ==========")

                for record in records:
                    print("-----------------------------------")
                    print(f"ID      : {record[0]}")
                    print(f"Name    : {record[1]}")
                    print(f"Subject : {record[2]}")
                    print(f"Hours   : {record[3]}")
                    print(f"Date    : {record[4]}")
                print("-----------------------------------")

        elif choice == "6":
            print("\nThank you for using Smart Study Hours Tracker!")
            break

        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    main()