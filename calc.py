# -*- coding: cp1252 -*-

def val():
    print "V�lj om du vill 1: Addera, 2: Subtrahera, 3: Multiplicera, 4: Dividera"
    val = raw_input("Skriv nummer h�r: ")
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
    plus1 = int(raw_input("Skriv f�rsta siffran: "))
    plus2 = int(raw_input("Skriv andra siffran: "))
    svar = plus1 + plus2
    print "Svaret �r ", svar

def subtrahera():
    minus1 = int(raw_input("Skriv f�rsta siffran: "))
    minus2 = int(raw_input("Skriv andra siffran: "))
    svar = minus1 - minus2
    print "Svaret �r ", svar

def multiplicera():
    ggr1 = int(raw_input("Skriv f�rsta siffran: "))
    ggr2 = int(raw_input("Skriv andra siffran: "))
    svar = ggr1 * ggr2
    print "Svaret �r ", svar

def dividera():
    dvd1 = int(raw_input("Skriv f�rsta siffran: "))
    dvd2 = int(raw_input("Skriv andra siffran: "))
    svar = dvd1 / dvd2
    print "Svaret �r ", svar

val()
