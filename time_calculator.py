import math
def add_time(start, duration, *Weekday):
  day = False
  for check in Weekday:
    day = check.capitalize()
  duration = duration.split(":")
  start = start.replace(":"," ").split(" ")
  weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  hours = int(start[0]) + int(duration[0])%24
  minutes = int(start[1]) + int(duration[1])
  daytime = start[2]
  day_count = math.trunc(int(duration[0])/24)
  
  'Calculate number of days passed'
  if daytime == "PM":
    if (math.trunc(minutes/60) + int(start[0])) >= 12 or hours >= 12:
      day_count = day_count + 1
      daytime = "AM"
  elif daytime == "AM":
    if (math.trunc(minutes/60) + int(start[0])) >= 12:
      daytime = "PM"

  if minutes == 60 or minutes == 0:
    minutes = "00"
    hours = hours + 1
  elif minutes < 10:
    minutes = "0" + str(minutes)
  elif minutes > 60 and minutes % 60 < 10:
    minutes = "0" + str(minutes % 60)
    hours = hours + 1
  elif minutes > 60:
    minutes = str(minutes % 60)
    hours = hours + 1
    
  if hours % 12 == 0:
    hours = 12
  else:
    hours = str(hours % 12)
    
  new_time = str(hours) + ":" + str(minutes) + " {}".format(daytime)
  if day != False:
    new_time = new_time + ", " + weekdays[(weekdays.index(day) + day_count) % 7]
  if day_count > 0: 
    if day_count == 1:
      new_time = new_time + " (next day)"
    else:
      new_time = new_time + " ({}".format(day_count) + " days later)"
  return new_time