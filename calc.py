# -*- coding: cp1252 -*-

def val():
    print "Välj om du vill 1: Addera, 2: Subtrahera, 3: Multiplicera, 4: Dividera"
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
    svar = dvd1 / dvd2
    print "Svaret är ", svar

val()
