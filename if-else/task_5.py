def days_in_year_till_date(a, b):
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    days_passed = sum(days_in_months[:b - 1]) + a
    return days_passed


def days_until_holidays(day, month):
    current_day_number = days_in_year_till_date(day, month)
    if 152 <= current_day_number:
        print("Каникулы начались!!!")
    else:
        print(f"До каникул осталось: {152-current_day_number}")

current_day = int(input("Введите число: "))
current_month = int(input("Введите месяц: "))


days_until_holidays(current_day, current_month)