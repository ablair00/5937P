import datetime
from datetime import timedelta

print("How far will you be driving today?:") 
mi = float(input("Miles:"))
driveSpeed = float(input("Average Driving Speed in MPH:"))
 
aveHours = round(mi/driveSpeed, 2) 
print("The trip will take on average " + str(aveHours) + " hour(s) to complete.") 

arrivalt = datetime.datetime.now() + timedelta(hours=aveHours)
arrivalt = arrivalt.strftime("%I:%M:%S %p")
print("If you leave now, you'll get there at", arrivalt) 
