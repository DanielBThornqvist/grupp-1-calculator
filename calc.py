# -*- coding: cp1252 -*-

import os

a = True

while a:

    def val():
        print "V�lj om du vill\n1: Addera\n2: Subtrahera\n3: Multiplicera\n\
4: Dividera\n5: Medeltal\n6: Median\n7: Summera flera tal\n8: Upph�jt till\n"
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

    def fortsatt():
        svar = raw_input("Vill du forts�tta? (Y/N): ")
        if svar.lower() == "y":
            a = True
            os.system("cls")
        elif svar.lower() == "n":
            exit()
        else:
            print "Fel input"
            fortsatt()
        

    def addera():
        plus1 = float(raw_input("Skriv f�rsta siffran: "))
        plus2 = float(raw_input("Skriv andra siffran: "))
        svar = plus1 + plus2
        print "Svaret: ",plus1,"+",plus2,"=",svar
        fortsatt()
        
    def subtrahera():
        minus1 = float(raw_input("Skriv f�rsta siffran: "))
        minus2 = float(raw_input("Skriv andra siffran: "))
        svar = minus1 - minus2
        print "Svaret: ",minus1,"-",minus2,"=",svar
        fortsatt()
        
    def multiplicera():
        ggr1 = float(raw_input("Skriv f�rsta siffran: "))
        ggr2 = float(raw_input("Skriv andra siffran: "))
        svar = ggr1 * ggr2
        print "Svaret: ",ggr1,"x",ggr2,"=",svar
        fortsatt()
        
    def dividera():
        dvd1 = float(raw_input("Skriv f�rsta siffran: "))
        dvd2 = float(raw_input("Skriv andra siffran: "))
        if dvd2 == 0:
            print "Error divide by 0"
            fortsatt()
        else:
            svar = dvd1 / dvd2
            print "Svaret: ",dvd1,"/",dvd2,"=",svar
            fortsatt()

    def medeltal():
        talarray = eval(raw_input("Skriv en array ex. [1, 2, 3, 4]"))
        svar = float (sum(talarray))/float(len(talarray))
        print "Medeltalet �r ", svar
        fortsatt()

    def median():
        talmedian = eval(raw_input("Skriv en array ex, [1, 2, 3, 4]"))
        sortera = sorted(talmedian)
        if len(sortera)%2 != 0:
            svar = sortera[len(sortera)/2]
            print svar
            fortsatt()
        else:
            var1 = float(sortera[len(sortera)/2])
            var2 = float((sortera[len(sortera)/2-1]))
            svar = float(((var1 + var2) / 2))
            print svar
            fortsatt()

    def summafler():
        summafler = eval(raw_input("Skriv de tal du vill addera som en array ex. [5, 10, 15]"))
        svar = float (sum(summafler))
        print "Svaret �r ", svar
        fortsatt()

    def upphojt():
        grund1 = int(raw_input("Skriv basen: "))
        grund2 = 1
        power = int(raw_input("Skriv vad du vill h�ja upp den till (Bara naturella tal som g�ller ^^): "))
        if power == 0:
            print 1
        x=1
        if grund2>0:
            while x<=power:
                grund2 = grund1*grund2
                x=x+1
        print "Svaret �r ", grund2
        fortsatt()

    val()
