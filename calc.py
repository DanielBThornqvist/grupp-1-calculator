# -*- coding: cp1252 -*-

def val():
    print "Välj om du vill 1: Addera, 2: Subtrahera, 3: Multiplicera, 4: Dividera , 5:Medeltal, 6: Median, 7: Summera flera tal, 8: Upphöjt till"
    val = raw_input("Skriv nummer här: ")
    if val == "1":
        print "Du har valt addera"
        addera()
    elif val == "2":
        print "Du har valt subtrahera"
        subtrahera()
    elif val == "3":
        print "Du har valt multiplicera"
        multiplicera()
    elif val == "4":
        print "Du har valt dividera"
        dividera()
    elif val == "5":
        medeltal()
    elif val == "6":
        median()
    elif val == "7":
        summafler()
    elif val == "8":
        upphojt()
    else:
        print "Error"
        

def addera():
    plus1 = int(raw_input("Skriv första siffran: "))
    plus2 = int(raw_input("Skriv andra siffran: "))
    svar = plus1 + plus2
    print "Svaret är ", svar

def subtrahera():
    minus1 = int(raw_input("Skriv första siffran: "))
    minus2 = int(raw_input("Skriv andra siffran: "))
    svar = minus1 - minus2
    print "Svaret är ", svar

def multiplicera():
    ggr1 = int(raw_input("Skriv första siffran: "))
    ggr2 = int(raw_input("Skriv andra siffran: "))
    svar = ggr1 * ggr2
    print "Svaret är ", svar

def dividera():
    dvd1 = int(raw_input("Skriv första siffran: "))
    dvd2 = int(raw_input("Skriv andra siffran: "))
    if dvd2 == 0:
        print "Error divide by 0"
    else:
        svar = dvd1 / dvd2
        print "Svaret är ", svar

def medeltal():
    talarray = eval(raw_input("Skriv en array ex. [1, 2, 3, 4]"))
    svar = float (sum(talarray))/float(len(talarray))
    print "Medeltalet är ", svar

def median():
    talmedian = eval(raw_input("Skriv en array ex, [1, 2, 3, 4]"))
    sortera = sorted(talmedian)
    if len(sortera)%2 != 0:
        for i in sortera:
            if i > (len(sortera)/2):
                svar = i - 1
                print svar
    else:
        for i in sortera:
            if i > (len(sortera)/2):
                svar = float(((i + (i - 1)) / 2))
                print svar

def summafler():
    summafler = eval(raw_input("Skriv de tal du vill addera som en array ex. [5, 10, 15]"))
    svar = float (sum(summafler))
    print "Svaret är ", svar

def upphojt():
    upp1 = int(raw_input("Skriv basen: "))
    upp2 = int(raw_input("Skriv vad du vill höja upp den till: "))
    elif upp2 == 0:
        print 1
    elif upp2 == 1:
        print upp1
    elif upp2 > 1
    svar = upp1 * 
    print "Svaret är ", svar

val()
