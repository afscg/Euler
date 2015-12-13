res = 0

year = 1900
month = 1
total = 1

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while year < 2001:
    total += days[month]
    if month == 2 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        total += 1
    month += 1
    if month > 12:
        month = 1
        year += 1
    if total % 7 == 0 and year > 1900:
        res += 1
print(res, year, month, total, total % 7)
