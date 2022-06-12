def LeapYear(num):
    if num % 4 == 0:
        if num % 100 != 0:
            print("it is a Leap year")
        elif num % 100 == 0:
            if num % 400 == 0:
                print("it is a Leap Year")
            else:
                print("not a Leap year")
    else:
        print("not a Leap year")


a = int(input("Year= "))
LeapYear(a)
