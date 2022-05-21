import datetime
import random


def check_if_leap_year(year: int):
    pass


def get_num_of_days_in_month(month: int, year: int):
    pass


def calculate_date(date: str, number_of_days: int):
    pass


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
