#1
from datetime import datetime, timedelta
current_data = datetime.now()
new_data = current_data - timedelta(days=5)
print("Current data: ", current_data.strftime("%Y-%m-%d"))
print("New data: ", new_data.strftime("%Y-%m-%d"))

#2
from datetime import datetime, timedelta
today = datetime.now().date()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("Yesterday: ", yesterday)
print("Today: ", today)
print("Tomorrow: ", tomorrow)

#3
from datetime import datetime
current_datatime = datetime.now()
without_microseconds = current_datatime.replace(microsecond=0)
print("Current datatime: ", current_datatime)
print("Without Microseconds: ", without_microseconds)

#4
from datetime import datetime
date1 = datetime(2024, 2, 1, 12, 0, 0)
date2 = datetime(2025, 2, 10, 14, 30, 0)
dif = abs((date2-date1).total_seconds())
print("Difference in seconds: ", dif)