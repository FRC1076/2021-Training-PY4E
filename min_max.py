def min_max():
    lst = []
    while True:
        num = input("Enter a number: ")
        if num == "done":
            try:
                lst.sort()
                min = lst[0]
                max = lst[-1]
                total = sum(lst)
                ave = total / len(lst)
            except:
                min = None
                max = None
                total = None
                ave = None
            print("Maximum is", max)
            print("Minimum is", min)
            print("Sum is", total)
            print("Average is", ave)
            break
        try:
            num = int(num)
            lst.append(num)
        except:
            print("Invalid input")

min_max()