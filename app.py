from db import create_table, insert_record, view_records

def main():
    create_table()

    while True:
        print("\n====================================")
        print("     Smart Study Hours Tracker")
        print("====================================")
        print("1. Add Study Record")
        print("2. View Study Records")
        print("3. Exit")

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
            print("\nThank you for using Smart Study Hours Tracker!")
            break

        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    main()