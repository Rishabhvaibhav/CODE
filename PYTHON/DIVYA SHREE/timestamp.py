from datetime import datetime

input_time = "2022-01-15 09:03:32.744178"



# Convert input to timestamp
timestamp = datetime.strptime(input_time, "%Y-%m-%d %H:%M:%S.%f")
# strptime() method date time string to a datetime object, aslo timstamp knows as string parse time
year = timestamp.year
month = timestamp.month
day = timestamp.day
time = timestamp.time()

print(year)
print(month)
print(day)
print(time)
