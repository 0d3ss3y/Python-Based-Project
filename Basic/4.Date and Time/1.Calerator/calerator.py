import calendar

def main():
    """Main function to display a calendar for a specific month or the whole year."""
    try:
        year = int(input("Enter year: "))

        month_selection = input("Do you want a specific month? [Y/N]: ").strip().upper()
        if month_selection == "Y":
            month = int(input("Enter month (1-12): "))
            if 1 <= month <= 12:
                print(calendar.month(year, month))
            else:
                print("Invalid month. Please enter a number between 1 and 12.")
        elif month_selection == "N":
            print(calendar.TextCalendar().formatyear(year))
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")
    except ValueError:
        print("Invalid input. Please enter numeric values for year and month.")

if __name__ == "__main__":
    main()
