day = 0
incidence = 219

above_300 = False
above_500 = False
above_1000 = False
above_10000 = False

# The loop simulates the incidence for every day
# Once it hits one of the given thresholds a message is printed
# To stop printing after the threshold is reached the flags above_xxx are used

while incidence <= 100000:
    day += 1
    incidence = int(incidence*1.0458)
    if incidence > 300 and not above_300:
        print(f"Über 300 an Tag {day}")
        above_300 = True
    if incidence > 500 and not above_500:
        print(f"Über 500 an Tag {day}")
        above_500 = True
    if incidence > 1000 and not above_1000:
        print(f"Über 1000 an Tag {day}")
        above_1000 = True
    if incidence > 10000 and not above_10000:
        print(f"Über 10000 an Tag {day}")
        above_10000 = True
    if incidence > 100000:
        print(f"Über 100000 an Tag {day}")
