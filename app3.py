import datetime
def print_header():
    print('-----------------------------')
    print('     Birthday App    ')
    print('-----------------------------')
    print()


def get_birthday_from_user():
    print("When were you born? ")
    year = int(input("Year [YYYY]: "))
    month = int(input("Month [MM]: "))
    day = int(input("Day [DD]: "))

    bday = datetime.date(year, month, day)
    return bday

def compute_days_between_two_dates(date1,date2):
    this_year_date = datetime.date(year=date2.year, month=date1.month, day=date1.day)
    td = this_year_date - date2
    return td.days


def print_birthday_information(number_of_days):

    print("You still have {} days until your birthday".format(number_of_days))


def main():
    print_header()
    bday = get_birthday_from_user()
    print(bday)
    today = datetime.date.today()
    number_of_days = compute_days_between_two_dates(bday, today)
    print_birthday_information(number_of_days)


main()