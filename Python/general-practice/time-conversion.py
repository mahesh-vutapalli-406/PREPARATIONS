# this program is to calculate/covert the time hours into seconds & minutes
import math
from math import floor, ceil

from botocore.compat import total_seconds

print("Enter the the hours\nNOTE: Enter time in 24 hours format & include minutes\nexample: 6.45 - for 6 hours 4 minutes Please don't add seconds)")
time = str(input())
hours = int(time.split('.')[0])
minutes = int(time.split('.')[1])

#checking the input

if hours > 24 or minutes > 59:
    print(f"Entered time {time} is wrong")
    exit(1)

#Converting the time into hours, minutes and seconds
print("*************************************************")
print(f"total time is {hours} hours and {minutes} minutes")
total_minutes = (hours * 60)+ minutes
print(f"total time in minutes - {total_minutes}")
total_seconds = total_minutes * 60
print(f"total time in seconds - {total_seconds}")
print("*************************************************")

course_completion_percentage = int(input("Enter the course completion % - "))

one_percent_of_course_minutes = total_minutes/100

total_course_minutes = total_minutes
total_completed_minutes = course_completion_percentage * one_percent_of_course_minutes
remaining_course_minutes = total_course_minutes - total_completed_minutes
print("*************************************************")
print(f"""

total course minutes - {total_course_minutes}
Percentage of course completed - {course_completion_percentage}

minutes of course completed - {total_completed_minutes}
minutes of course remaining - {remaining_course_minutes}

""")
print("*************************************************")

