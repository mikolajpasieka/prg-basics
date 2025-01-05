###
# Returns the name of the day of the week for a given day number (1-Monday ... 7-Sunday)
#
def weekday(n):
 weekdays = ["Monday", "Tuesday", "Wednesday",
         "Thursday", "Friday", "Saturday", "Sunday"]
 return weekdays[n-1]

if __name__ == "__main__":
 print(weekday(1))
 print(weekday(2))
 print(weekday(3))
 print(weekday(4))
 print(weekday(5))
 print(weekday(6))
 print(weekday(7))

