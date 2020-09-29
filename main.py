
age=input('how old are you? ')
daymonth=input('what is the current day of the month? ')
month=input('what is the current month? ')
boolbirthday=input('did you have your birthday yet? ')
year = input('what year is it? ')
bornmonth=input('in what month were you born? ')
borndaymonth=input('on what day of the month were you born? ')


borndaymonth=int(borndaymonth)
age=int(age)
daymonth=int(daymonth)
year=int(year)

if year % 4 == 0:
    h = 29
else:
    h = 28



if boolbirthday == 'no':
    print('ok')
elif boolbirthday == 'yes':
    print('ok')
    age=age-1
else:
    print('i do not understand')
        

g=age*365
g=g+daymonth

if month == 'jan':
    pass
elif month == 'feb':
    g=g+31
elif month== 'mar':
    g=g+h+31
elif month == 'apr':
    g=g+h+31+h+31
elif month == 'may':
    g=g+31+h+31+30
elif month == 'jun':
    g=g+31+h+31+30+31
elif month == 'jul':
    g=g+31+h+31+30+31+31
elif month == 'aug':
    g=g+31+h+31+30+31+30+31
elif month == 'sep':
    g=g+31+h+31+30+31+30+31+31
elif month == 'oct':
    g=g+31+h+31+30+31+30+31+31+30
elif month == 'nov':
    g=g+31+h+31+30+31+30+31+31+30+31
elif month == 'dec':
    g=g+31+h+31+30+31+30+31+31+30+31+30


yearborn = year - age + 1
if yearborn % 4 == 0:
    h = 29
else:
    h = 28


if bornmonth == 'jan':
    g=g+h+31+30+31+30+31+31+30+31+30+31
    g=g+31-k
elif bornmonth == 'feb':
    g=g+31+30+31+30+31+31+30+31+30+31
    g=g+h-k
elif bornmonth == 'mar':
    g=g+30+31+30+31+31+30+31+30+31
    g=g+31-k
elif bornmonth == 'apr':
    g=g+31+30+31+31+30+31+30+31
    g=g+30-k
elif bornmonth == 'may':
    g=g+30+31+31+30+31+30+31
    g=g+31-k
elif bornmonth == 'jun':
    g=g+31+31+30+31+30+31
    g=g+30-k
elif bornmonth == 'jul':
    g=g+31+30+31+30+31
    g=g+31-k
elif bornmonth == 'aug':
    g=g+30+31+30+31
    g=g+31-k
elif bornmonth == 'sep':
    g=g+31+30+31
    g=g+30-k
elif bornmonth == 'oct':
    g=g+30+31
    g=g+31-k
elif bornmonth == 'nov':
    g=g+31
    g=g+30-k
elif bornmonth == 'dec':
    g=g+31-k



# Calculate extra leap days

nextleap = 4 - (yearborn % 4) + yearborn

g = g + ((year-nextleap) // 4) + 1


g=g+1

if boolbirthday == 'no':
    print('ok')
elif boolbirthday == 'yes':
    print('ok')
    q=q+1
else:
    print('i do not understand')


print('you have been alive for',g,'days and',q,'yers old')   

























