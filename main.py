import datetime
import random


def check_if_leap_year(year: int):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def get_num_of_days_in_month(month: int, year: int):
    """
    Returns a number of days in a given month.
    :param month: integer variable in range from 1 to 12.
    :param year: integer variable to check is year leap or not.
    :return: integer, number of days in a given month.
    """
    month_values = {"thirty one": [1, 3, 5, 7, 8, 10, 12],
                    "thirty": [4, 6, 9, 11],
                    "twenty eight or nine": [2]}
    if month in month_values["thirty one"]:
        result = 31
    elif month in month_values["thirty"]:
        result = 30
    else:
        result = 29 if check_if_leap_year(year) else 28
    return result


def calculate_date(date: str, number_of_days: int):
    """
    Takes a date if format dd.mm.yyyy and a number of days, that should be added to the date. Returns incremented date.
    :param date: string, that represents date that should be incremented. Format for date is dd.mm.yyyy
    :param number_of_days: integer, that represent a number of days that should be added to the date.
    :return: string, that represents changed date. Format for date is dd.mm.yyyy
    """
    date = date.split(".")
    date = [int(num) for num in date]
    date = {"day": date[0], "month": date[1], "year": date[2]}
    while number_of_days:
        days_in_month = get_num_of_days_in_month(date["month"], date["year"])
        added_days_to_month = days_in_month - date["day"] + 1
        if number_of_days >= added_days_to_month:
            date["day"] = 1
            date["month"] = date["month"] + 1 if date["month"] != 12 else 1
            date["year"] = date["year"] + 1 if date["month"] == 1 else date["year"]
            number_of_days -= added_days_to_month
        else:
            date["day"] += number_of_days
            break
    return ".".join(["0" + str(num) if len(str(num)) == 1 else str(num) for num in list(date.values())])


def test_implementation(foo):
    """
    Test function to check the implementation of the main function algorithm.
    Audition process is based on datetime module functions.
    :param foo: function with implementation of date incrementation algorithm.
    :return: None object, all the information is printed in the standard output window.
    """
    passed_tests = 0
    failed_tests = 0
    test_cases = 1000
    failed_examples = {"function value": [], "should be": []}
    start_date = datetime.date(1990, 1, 1)
    end_date = datetime.date(2030, 1, 1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days

    for _ in range(test_cases):
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        number_of_days = random.randint(1, 10000)

        date_to_compare = random_date + datetime.timedelta(days=number_of_days)
        date_to_compare = str(date_to_compare).split("-")
        date_to_compare = date_to_compare[2] + "." + date_to_compare[1] + "." + date_to_compare[0]

        date_to_check = str(random_date).split("-")
        date_to_check = date_to_check[2] + "." + date_to_check[1] + "." + date_to_check[0]
        date_to_check = foo(date_to_check, number_of_days)

        if date_to_check != date_to_compare:
            failed_tests += 1
            failed_examples["function value"].append(date_to_check)
            failed_examples["should be"].append(date_to_compare)
        else:
            passed_tests += 1
    if failed_tests:
        print("Tests failed in cases:")
        for test in range(failed_tests):
            print("Should be: {}, but function returned: {}".format(failed_examples["should be"][test],
                                                                    failed_examples["function value"][test]))
    print("Test passed: {}/{}".format(passed_tests, test_cases))


if __name__ == "__main__":
    test_implementation(calculate_date)
    print("Manual test number 1:", calculate_date("10.01.2008", 10))
    print("Manual test number 2:", calculate_date("29.06.2020", 8))
