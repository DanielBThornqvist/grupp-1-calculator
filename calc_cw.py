# -*- coding: cp1252 -*-

def val():
    metod = raw_input("1= plus, 2 = minus , 3 = multi, 4 = divi, 5 = medeltal")
    if metod == "1":
        add()
    elif metod == "2":
        minus()
    elif metod == "3":
        multi()
    elif metod == "4":
        divi()
    elif metod == "5":
        medeltal()
    elif metod == "6":
        median()
    else:
        print"Error"
    
def add():
    a = int(raw_input("Första"))
    b = int(raw_input("Andra"))
    c = a + b
    print a ,"+", b ,"=", c
def minus():
    a = int(raw_input("Första"))
    b = int(raw_input("andra"))
    c = a - b
    print a ,"-", b ,"=", c
def multi():
    a = int(raw_input("Första"))
    b = int(raw_input("andra"))
    c = a * b
    print a ,"*", b ,"=", c
def divi():
    a = float(raw_input("Första"))
    b = float(raw_input("andra"))
    c = a / b
    print a ,"/", b ,"=", round(c,3)
def medeltal():
    a = int (raw_input("Första"))
    b = int(raw_input("andra"))
    c = (a+b) /2
    print "medeltalet mellan", a, "och" ,b, "är", c
def median():
    talmedian = eval(raw_input("Skriv en array ex, [1, 2, 3, 4]"))
    sortera = sorted(talmedian)
    if len(sortera)%2 == 0:
        for i in sortera:
            if i > (len(sortera)/2):
                svar = float(i - 1)
                print svar
    else:
        for i in sortera:
            if i > (len(sortera)/2):
                svar = float(((i + (i - 1)) / 2))
                print svar
def upph():
    
