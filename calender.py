
no_leapyear = {}    # {0: 365, 1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
leapyear = {}       # {0: 366, 1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
month_name = ["     ", "JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]
x_ = [int(i) for i in range(13)]
for j in x_:
    if j == 0:
        no_leapyear[j] = 365
    elif j == 1 or j == 3 or j == 5 or j == 7 or j == 8 or j == 10 or j == 12:
        no_leapyear[j] = 31
    elif j == 2:
        no_leapyear[j] = 28
    else:
        no_leapyear[j] = 30
leapyear = no_leapyear.copy()
leapyear[0] += 1
leapyear[2] += 1

weekday = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

Y = int(input('Please enter year: '))
M = int(input('Please enter month (0 ⇨ annual calender): '))


def judge_leap(year):
    if Y%100 == 0 and Y%400 != 0:
        return no_leapyear
    elif Y%4 == 0:
        return leapyear
    else:
        return no_leapyear

def zeller_(year, month, day):

    if month <= 2:
        year -= 1
        month += 12

    month -= 2
    w = day + int((13 * month - 1) / 5) + year + int(year / 4) - int(year / 100) + int(year / 400)
    X = w % 7
    return X


if M == 0:
    sMonth = 1
    eMonth = 12
else:
    sMonth = M
    eMonth = M

print("-----------------------------------")
print("YEAR: " + str(Y))

for loop in range(sMonth, eMonth+1):
    
    if sMonth <= loop <= eMonth:
        print("MONTH: " + month_name[loop])
        print()
        print(*weekday, sep="  ")

    cnt = 0
    print(("     ") * (int(zeller_(Y, loop, 1))), end="")
    cnt += int(zeller_(Y, loop, 1))
    for d in range(1, judge_leap(Y)[loop]+1):
        print("{:3}".format(d), end="  ")
        cnt += 1
        if cnt%7 == 0:
            print()
    print()
    print("-----------------------------------")



