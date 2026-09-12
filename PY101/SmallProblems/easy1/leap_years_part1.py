def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return year % 4 == 0

print(is_leap_year(1))
print(is_leap_year(2))
print(is_leap_year(3))
print(is_leap_year(4))
print(is_leap_year(1000))
print(is_leap_year(1100))
print(is_leap_year(1200))
print(is_leap_year(1300))
print(is_leap_year(1751))
print(is_leap_year(1752))
print(is_leap_year(1753))
print(is_leap_year(1800))
print(is_leap_year(1900))
print(is_leap_year(2000))
print(is_leap_year(2023))
print(is_leap_year(2024))
print(is_leap_year(2025))
