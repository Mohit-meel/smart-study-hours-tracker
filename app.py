def main():
    print("====================================")
    print("    Smart Study Hours Tracker")
    print("====================================")

    name = input("Enter your name: ")
    hours = float(input("Enter study hours for today: "))

    print("\nStudy Record")
    print(f"Student: {name}")
    print(f"Study Hours: {hours}")

if __name__ == "__main__":
    main()