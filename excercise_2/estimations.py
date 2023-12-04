import math
import inflect
from datetime import timedelta

def convert_seconds_to_readable_time(seconds):
    # Calculate years, days, hours, minutes, and seconds
    years, remainder = divmod(seconds, 60*60*24*365)
    days, remainder = divmod(remainder, 60*60*24)
    hours, remainder = divmod(remainder, 60*60)
    minutes, seconds = divmod(remainder, 60)

    # Build a readable string
    time_string = ""
    if years:
        time_string += f"{int(years)} years, "
    if days:
        time_string += f"{int(days)} days, "
    if hours:
        time_string += f"{int(hours)} hours, "
    if minutes:
        time_string += f"{int(minutes)} minutes, "
    if seconds:
        time_string += f"{int(seconds)} seconds"

    return time_string.rstrip(', ')

p = inflect.engine()

# Calculate the number of possible passwords for each system
base = 62 #number of possible characters

system_1_passwords = base**5
system_2_passwords = base**10
system_3_passwords = sum(base**i for i in range(5, 11))

print("System 1:", system_1_passwords, 
      "\t\t = ", 
      f"{round(system_1_passwords / 10**(int(math.log10(system_1_passwords))), 3)} x 10^{int(math.log10(system_1_passwords))}",
      "->\n", 
      p.number_to_words(system_1_passwords),
      "\n"
      )
print("System 2:", system_2_passwords, 
      "\t = ", f"{round(system_2_passwords / 10**(int(math.log10(system_2_passwords))), 3)} x 10^{int(math.log10(system_2_passwords))}",
      "->\n", 
      p.number_to_words(system_2_passwords),
      "\n"
      )
print("System 3:", system_3_passwords, 
      "\t = ", f"{round(system_3_passwords / 10**(int(math.log10(system_3_passwords))), 3)} x 10^{int(math.log10(system_3_passwords))}",
      "->\n", 
      p.number_to_words(system_3_passwords),
      "\n"
      )

#Calculate the time with brute Force
print("Estimated Time with brute force")
# Assuming the system can check 1_000_000 combinations per second
combinations_per_second = 1_000_000
# Calculate the time in seconds
time_seconds_system1 = system_1_passwords / combinations_per_second
time_seconds_system2 = system_2_passwords / combinations_per_second
time_seconds_system3 = system_3_passwords / combinations_per_second

print("System 1 Brute Force time: ", convert_seconds_to_readable_time(time_seconds_system1))
print("System 2 Brute Force time: ", convert_seconds_to_readable_time(time_seconds_system2))
print("System 3 Brute Force time: ", convert_seconds_to_readable_time(time_seconds_system3))
