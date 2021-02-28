import datetime
from datetime import timedelta

print("Adds 2 years to the current day and subtracts 60 seconds from the current time:") 
future = datetime.datetime.now() - timedelta(seconds=60) + timedelta(days=730)
future = future.strftime("%a,%b,%d,%Y @ %I:%M:%S %p")
print(future)
