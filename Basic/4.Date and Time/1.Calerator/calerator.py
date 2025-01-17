import calendar

def main():
   year = int(input("Enter year: "))

   month_selection = input("Do you want a specific month?[Y/N] ").upper()[0]
   if month_selection == "Y":
       month = int(input("Enter month: "))
       print(calendar.month(year, month))


    elif month_selection == "N":
        print(calendar.month(year))
   else:
       print("Invalid input")


if __name__ == '__main__':
    main()