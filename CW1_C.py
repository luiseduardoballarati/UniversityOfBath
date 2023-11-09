"""
INSTRUCTIONS:

18/05/2007 was a Tuesday
Months with 30 days: 4, 6, 9, 11
Months with 31 days: 1, 3, 5, 7, 8, 10, 12
February: 28 days and 29 on leap years.
To be a leap year, the year number must be divisible by four
– except for end-of-century years, which must be divisible by 400.
This means that the year 2000 was a leap year, although 1900 was not.
2024, 2028, 2032 and 2036 are all leap years.

How many mondays fell on 12th of the month between 1 Jan 1401 and 31 Dec 1800?
"""
def is_it_leap_year(year):
    year = str(year)
    if int(year) % 4 == 0 and year[2:4] != '00':
        return True
    if year[2:4] == '00' and int(year) % 400 == 0:
        return True
    else:
        return False

def days_between(start, end):
    days = 0
    year = start
    while year <= end:
        if is_it_leap_year(year):
            days += 366
        else:
            days += 365
        year += 1
    return days

def common_data(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result
    return result


def number_of_elements(list1, list2):
    a_set = set(list1)
    b_set = set(list2)

    if len(a_set.intersection(b_set)) > 0:
        return len(a_set.intersection(b_set))
    else:
        return 0

def howManyDays():
    days = (days_between(1401, 2007))

    # 227 is the number of days left in 2007 to be 31/12/2007.
    days = days-227
    #print(f"The difference in days between 01/01/1401 and 18/05/2007 is {days}")
    #print((days) % 7) # Monday
    #print(f"01/01/1401 was a Monday")

    var = (days_between(1401, 1800))
    # 01/01/1401 -> 01/01/1801
    #print(var)
    # 01/01/1401 -> 31/12/1800
    #print(var-1)
    mondays = []
    for monday in range(1, var, 7):
        mondays.append(monday)

    normal_year_day_12 = [12, 43, 71, 102, 132, 162, 193, 223, 254, 285, 315, 346]
    res = 0
    year = 1401

    while year <= 1800:
        if common_data(mondays, normal_year_day_12):
            number = number_of_elements(mondays, normal_year_day_12)
            res += number
        if is_it_leap_year(year):
            for i in range(len(normal_year_day_12)):
                normal_year_day_12[i] += 366
        else:
            for i in range(len(normal_year_day_12)):
                normal_year_day_12[i] += 365
        year += 1

    return (res)

print(howManyDays())