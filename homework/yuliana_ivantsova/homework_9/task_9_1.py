import datetime

date = "Jan 15, 2023 - 12:05:33"

python_date = datetime.datetime.strptime(date, "Jan %d, %Y -  %H:%M:%S")
month = python_date.strftime("%B")
formate_date = python_date.strftime("%d.%m.%Y, %H:%M")

print(month)
print(formate_date)
