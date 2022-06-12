def GradeCalc(num):
    if num < 25:
        print('F')
    elif num >= 25 and num < 45:
        print('E')
    elif num >= 45 and num < 50:
        print('D')
    elif num >= 50 and num < 60:
        print('C')
    elif num >= 60 and num < 80:
        print('B')
    else:
        print('A')


a = int(input("Enter total marks= "))
GradeCalc(a)
