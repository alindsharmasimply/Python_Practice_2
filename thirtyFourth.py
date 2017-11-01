import calendar
mm, dd, yy = map(int, raw_input().split())
print list(calendar.day_name)[calendar.weekday(yy, mm, dd)].upper()
