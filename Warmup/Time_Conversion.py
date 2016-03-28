from datetime import datetime

time = datetime.strptime(input().strip(), "%I:%M:%S%p")
print (datetime.strftime(time, "%H:%M:%S"))
