currentMax = None
currentMin = None

while (True):
    try:
        number = input("Input a number")
        if number == 'Done':
            break
        if number > currentMax:
            currentMax = number
        if number < currentMin:
            currentMin = number
    except:
        print("Not a number")

print("Maximum: " + currentMax)
print("Minimum: " + currentMin)

#change