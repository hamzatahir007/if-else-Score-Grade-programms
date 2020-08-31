hrs = input("Enter Hours:")
istrg= float(hrs)
rate= input("Enter Rate:")
astrg= float(rate)

pay = (istrg * astrg)

if pay < 500 :
    print(pay)
else :
    print('not a number')
