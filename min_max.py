largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try: 
        n=float(num)
    except:
        print("error")
    if largest is None or n>largest:
        largest=n
    if smallest is None or n<smallest:
        smallest=n
    print(num)

print("Maximum", largest)
print("Minimum", smallest)
  git config --global user.email "miazsanborn@gmail.com"
  git config --global user.name "Miazsanborn1"