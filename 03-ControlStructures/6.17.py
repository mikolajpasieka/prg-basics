time = input("Enter time (24-hour format):")
if int(time[0:2]) <=12:
    print(f"{time}am")
else:
    h = int(time[0:2])-12
    m = time[3:5]
    print(f"{h}:{m}pm")
