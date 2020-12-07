def min_max():
    lst = []
    while True:
        num = input("Enter a number: ")
        if num == "done":
            try:
                lst.sort()
                min = lst[0]
                max = lst[-1]
            except:
                min = None
                max = None
            print("Maximum is", max)
            print("Minimum is", min)
            break
        try:
            num = int(num)
            lst.append(num)
        except:
            print("Invalid input")

min_max()