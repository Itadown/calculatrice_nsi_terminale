# -*- coding: utf-8 -*-
from tkinter import *
from random import randrange
from PIL import Image
from math import exp, sqrt, pi
import time


#  ╔═══════════════════════════════════════╗
#  ║          Calculatrice Python          ║
#  ║                Made by                ║
#  ║     Dylan BAUDIN and Hugo GRAFFIN     ║
#  ╚═══════════════════════════════════════╝





#    Schéma démonstratif, paterne contracté
#
#    ╔════════════════╗
#    ║              ~ ║ <═══════ Historique contenant le précédent résulat / calcul
#    ║              0 ║
#    ║----------------║
#    ║  C  DEL  %   ÷ ║
#    ║                ║
#    ║  7   8   9   X ║
#    ║                ║
#    ║  4   5   6   - ║
#    ║                ║
#    ║  1   2   3   + ║
#    ║                ║
#    ║  ¤   0   ,   = ║
#    ╚════════════════╝
#       ^
#       ╚═══════════════════════ Extension de la calculatrice pour avoir plus de fonction (La plupart ne fonctionnant qu'avec le mode normal)





#    Schéma démonstratif, paterne étendue
#
#    ╔════════════════════╗
#    ║                  ~ ║
#    ║                  0 ║
#    ║--------------------║
#    ║  X!  X   √   π  1/x║
#    ║                    ║
#    ║  ±   C  DEL  %   / ║
#    ║                    ║
#    ║  X²  7   8   9   X ║
#    ║                    ║
#    ║  △  4   5   6   - ║
#    ║                    ║
#  ╔>║  ↔   1   2   3   + ║
#  ║ ║                    ║
#  ║ ║  ¤   e   0   ,   = ║
#  ║ ╚════════════════════╝
#  ║
#  ╚════════════════════════════ Menu permettant de choisir le mode de fonctionnement de la calculatrice



class Pile :
    def __init__(self):
        self.lst = []

    def est_vide(self):
        if self.lst == [] :
            return True
        else:
            return False

    def empiler(self, e):
        self.lst.append(e)
        return self.lst

    def sommet(self):
        if self.est_vide() == True :
            return
        else:
            return self.lst[-1]

    def depiler(self):
        assert(self.lst != []),'erreur'
        return self.lst.pop()

    def __str__(self):
        self.str = ""
        for i in range(len(self.lst)):
            self.str =   str(self.str) + str('|') + str(self.lst[-1-i]) + str('|') + str('\n')
        return str(self.str)

    def int_(self, str):
        if type(str) == str:
            return int(str)
        else:
            return str


def calculnormal():
    """
    La fonction calculnormal ne prend aucun paramètre. Elle permet,
    lorsque la calculatrice est en mode normal, de résoudre le calcul
    donné par l'utilisateur. Elle renvoit une chaine de caractère
    contenant le resultat du calcul
    """
    global ecrit
    def split(word):
        """
        La fonction split prend en paramètre une chaine de caractère.
        Elle permet de transformer cette dernière en tableau.
        Elle renvoit un tableau
        """
        return [char for char in word] #Transforme la chaine de caractère en tableau

    tableau = split(ecrit)

    new = []
    i = 0

    while i < len(tableau):
        varNow = 0
        if tableau[i].isnumeric() and tableau[i] != "²" or tableau[i] == "." or tableau[i] == "-": #On vérifie si tableau[i] est transformable en entier, s'il est différent de "²", si c'est un "." ou si c'est un "-"
            varNow = tableau[i]
            i += 1
            if i < len(tableau) :
                while tableau[i].isnumeric() and tableau[i] != "²" or tableau[i] == "." or tableau[i] == "-":
                    varNow += tableau[i]
                    i+=1
                    if i >= len(tableau) :
                        break #On force la sortie de la boucle
            new.append(varNow)
        else :
            new.append(tableau[i])
            i += 1
    print(new)
    def calcul (a, b):
        """
        La fonction calcul prend en paramètre deux caractères a et b.
        Elle permet de réaliser les calculs en prenant en compte les
        priorités mathématiques.
        """
        if a == "π" and b =="&" :

            if firstDiv < firstMul:
                print (new)
                i = firstDiv
                new[i] = round(pi, 2)
            else :
                i = firstMul
                new[i] = float(new[i-1])**-1
                new.pop(i-1)

        if a == "^" and b == "e" :

            if firstDiv < firstMul:
                i = firstDiv
                new[i] = float(new[i-1])**float(new[i+1])
                new.pop(i+1)
                new.pop(i-1)
            else :
                i = firstMul
                new[i] = round(exp(1), 3)

        if a == "√" and b =="²" :

            if firstDiv < firstMul:
                i = firstDiv
                new[i] = round(sqrt(float (new[i+1])),2)
                new.pop(i+1)
            else :
                i = firstMul
                new[i] = float(new[i-1])**2
                new.pop(i-1)

        if a == "/" and b =="x" :

            if firstDiv < firstMul:
                i = firstDiv
                new[i] = round(float (new[i-1]) / float (new[i+1]),2)
                new.pop(i-1)
                new.pop(i)
            else :
                i = firstMul
                new[i] = float (new[i-1]) * float(new[i+1])
                new.pop(i-1)
                new.pop(i)

        if a == "+" and b == "–":

            if firstDiv < firstMul:
                i = firstDiv
                new[i] = float (new[i-1]) - float (new[i+1])
                new.pop(i-1)
                new.pop(i)
            else :
                i = firstMul
                new[i] = float (new[i-1]) + float(new[i+1])
                new.pop(i-1)
                new.pop(i)

    while "!" in new :
        i = new.index('!')
        new[i] = factorielle(new[i-1])
        new.pop(i-1)

    while "π" in new or "&" in new:
        if "π" in new :
            firstDiv = new.index('π') #On regarde si le caractère se trouve dans notre tableau; si c'est le cas, on récupère sa première occurence
        else :
            firstDiv = 99999999 #On initialise un gros chiffre pour ne pas être embêté par la suite
        if "&" in new :
            firstMul = new.index('&')
        else :
            firstMul = 99999999
        calcul("π", "&")

    while "^" in new or "e" in new:
        if "^" in new :
            firstDiv = new.index('^')
        else :
            firstDiv = 99999999
        if "e" in new :
            firstMul = new.index('e')
        else :
            firstMul = 99999999
        calcul("^", "e")

    while "√" in new or "²" in new :
        if "√" in new :
            firstDiv = new.index('√')
        else :
            firstDiv = 99999999
        if "²" in new :
            firstMul = new.index('²')
        else :
            firstMul = 99999999
        calcul("√","²")

    while "/" in new or "x" in new :
        if "/" in new :
            firstDiv = new.index('/')
        else :
            firstDiv = 99999999
        if "x" in new :
            firstMul = new.index('x')
        else :
            firstMul = 99999999
        calcul("/","x")

    while "–" in new or "+" in new :
        if "–" in new :
            firstDiv = new.index('–')
        else :
            firstDiv = 99999999
        if "+" in new :
            firstMul = new.index('+')
        else :
            firstMul = 99999999
        calcul("+","–")

    ecrit = "".join(map(str, new)) #On transforme le tableau en chaine de caractère
    text.set(ecrit)


def calculpologne():
    """
    La fonction caluclpologne ne prend aucun paramètre et a pour objectif d'effectuer les calculs
    en notation polonaise inversé, mais aussi à savoir si on est passé en calcul normal (avec la
    variable chang), à résoudre delta, a vérifier si le calcul est correctement écrit, à faire les exposants,
    factorielles (la variable anc sert à faire l'historique grisé).
    """
    global ecrit, calcul, deltasolv, ancien, mem

    if "&" in ecrit :
        ancien = memoireinverse
    else :
        ancien = ecrit

    if deltasolv == 1 :
        return solv(a, b, c)

    if chang == 1 :
        calculnormal()
        return

    calculfait = False
    pile = Pile()
    tabsign = ['x', '–', '+', '/', '²']
    tot = 0
    longueur = len(calcul.lst)


    for j in range(0, len(calcul.lst)):
        if calcul.lst[j] in tabsign:
            tot -= 1
        else:
            tot += 1

    if tot != 1:
        text.set("Erreur")
        return


    for i in calcul.lst:
        if i in tabsign : # Si le signe est dans le tableau
            nb1 = pile.depiler()
            neg1 = 0
            neg2 = 0

            if pile.est_vide() == True:
                text.set("Erreur")
                return

            nb2 = pile.depiler()



            if type(nb1) == list: #Condition pour pouvoir faire plusieurs exposants à nb1 ou nb2
                while type(nb1[0]) == list: #Boucle nécessaire pour mettre les exposant à nb1
                    if type(nb1[0][0]) == list:
                        if type(nb1[0][0][0]) == list:
                            if type(nb1[0][0][0][0]) == list:
                                if type(nb1[0][0][0][0][0]) == list: #Condition pour limiter le nombre d'exposant à 5
                                    text.set("Erreur")
                                    return
                                nb1[0][0][0][0] = nb1[0][0][0][0][0] ** nb1[0][0][0][0][2]
                            nb1[0][0][0] = nb1[0][0][0][0] ** nb1[0][0][0][2]
                        nb1[0][0] = nb1[0][0][0] ** nb1[0][0][2]
                    nb1[0] = nb1[0][0] ** nb1[0][2]
                nb1 = nb1[0] ** nb1[2]

            else:
                nb1 = str(nb1)

            if nb1[0] == "-":
                neg1 = 1
                nb1 = nb1[1:] #On récupère la chaine de caractère nb1 sans le premier caractère
            if nb1[-1] == "!":
                nb1 = str(factorielle(nb1[:-1])) #On lance la fonction factorielle avec la chaine de caractère sans son dernier caractère (caractère correspondant au "!")
            if nb1.isnumeric() == True:
                nb1 = int(nb1)
            else:
                nb1 = float(nb1)
            if neg1 == 1:
                nb1 = -nb1



            if type(nb2) == list:
                while type(nb2[0]) == list:
                    if type(nb2[0][0]) == list:
                        if type(nb2[0][0][0]) == list:
                            if type(nb2[0][0][0][0]) == list:
                                if type(nb2[0][0][0][0][0]) == list:
                                    text.set("Erreur")
                                    return
                                nb2[0][0][0][0] = nb2[0][0][0][0][0] ** nb2[0][0][0][0][2]
                            nb2[0][0][0] = nb2[0][0][0][0] ** nb2[0][0][0][2]
                        nb2[0][0] = nb2[0][0][0] ** nb2[0][0][2]
                    nb2[0] = nb2[0][0] ** nb2[0][2]
                nb2 = nb2[0] ** nb2[2]

            else:
                nb2 = str(nb2)

            if nb2[0] == "-":
                neg2 = 1
                nb2 = nb2[1:]
            if nb2[-1] == "!":
                nb2 = str(factorielle(nb2[:-1]))
            if nb2.isnumeric() == True:
                nb2 = int(nb2)
            else:
                nb2 = float(nb2)
            if neg2 == 1:
                nb2 = -nb2



            if i == 'x':
                result = nb1 * nb2
                pile.empiler(result)
            if i == '+':
                result = nb1 + nb2
                pile.empiler(result)
            if i == '–':
                result = nb2 - nb1
                pile.empiler(result)
            if i == '/':
                result = nb2 / nb1
                pile.empiler(result)
            calculfait = True

        else:
            pile.empiler(i)

    if calculfait == True:
        nbre = pile.depiler()
    if pile.est_vide() == False:
        nb = pile.depiler()
        nbstr = str(nb)
        if type(nb) == list:
            while type(nb[0]) == list: #Nouvelle boucle pour le cas où l'utilisateur demande l'exposant que d'un nombre, exemple : 2^3^4^9
                if type(nb[0][0]) == list:
                    if type(nb[0][0][0]) == list:
                        if type(nb[0][0][0][0]) == list:
                            if type(nb[0][0][0][0][0]) == list:
                                text.set("Erreur")
                                return
                            nb[0][0][0][0] = nb[0][0][0][0][0] ** nb[0][0][0][0][2]
                        nb[0][0][0] = nb[0][0][0][0] ** nb[0][0][0][2]
                    nb[0][0] = nb[0][0][0] ** nb[0][0][2]
                nb[0] = nb[0][0] ** nb[0][2]
            nb = nb[0] ** nb[2]
        elif nbstr[-1] == "!":
            nb = factorielle(nbstr[:-1])
        pile.empiler(nb)
    if calculfait == True:
        pile.empiler(nbre)

    neg = 0
    ecrit = str(round(pile.sommet(), 2)) #On arrondit à deux chiffres après la virgule
    ecrit2 = ecrit
    mem = ancien
    clear_pile()
    anc.set(mem)
    if ecrit2[0] == "-":
        neg = 1
        ecrit2 = ecrit2[1:]
    if ecrit2.isnumeric() == True: #On vérifie que ecrit2 est transformable en entier
        if neg == 1:
            ecrit2 = "-" + ecrit2
        calcul.empiler(int(ecrit2))
    else:
        if neg == 1:
            ecrit2 = "-" + ecrit2
        calcul.empiler(float(ecrit2))

    text.set(ecrit2)
    ecrit = ecrit2
    return ecrit




def changement():
    """
    La fonction changement ne prend aucun paramètre. Elle permet à
    l'utilisateur d'agrandir la calculatrice ou de la rétracter (voir schéma).
    Elle ne renvoit rien.
    """
    global extend, chang, button_posneg, button_carre, button_menu, button_delta, button_exponentielle, AffichageCalcul, button_factorielle, button_racinecarre, AffichageCalcul1, AffichageCalcul2, AffichageCalcul3, button_0, button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9, button_switch, button_egal, button_clear, button_pourcentage, button_suppr, button_virgule, button_diviser, button_multiplier, button_additionner, button_soustraire, button_exposant, button_pi, button_inverse
    extend = extend + 1
    if extend % 2 == 0 :

        button_7.destroy()
        button_8.destroy()
        button_9.destroy()
        button_4.destroy()
        button_5.destroy()
        button_6.destroy()
        button_1.destroy()
        button_2.destroy()
        button_3.destroy()
        button_0.destroy()

        button_switch.destroy()
        button_egal.destroy()
        button_clear.destroy()
        button_pourcentage.destroy()
        button_suppr.destroy()
        button_virgule.destroy()
        button_diviser.destroy()
        button_multiplier.destroy()
        button_soustraire.destroy()
        button_additionner.destroy()

        AffichageCalcul3.destroy()
        AffichageCalcul2.destroy()
        AffichageCalcul1.destroy()

        AffichageCalcul3 = Entry(font = ('arial', 20, 'bold'), fg = 'white', readonlybackground = 'black', state = 'readonly', bd = 0, selectborderwidth = 100, insertwidth = 40, bg = 'black', justify = 'right')
        AffichageCalcul3.grid(row = 0, column =  1, columnspan = 5)
        AffichageCalcul2 = Entry(font = ('arial', 16, 'bold'), fg = 'gray', readonlybackground = 'black', state = 'readonly', textvariable = anc, bd = 0, selectborderwidth = 100, insertwidth = 40, bg = 'black', justify = 'right')
        AffichageCalcul2.grid(row = 1, column = 1, columnspan = 5)
        AffichageCalcul1 = Entry(font = ('arial', 16, 'bold'), fg = 'white', readonlybackground = 'black', state = 'readonly', textvariable = text, bd = 0, selectborderwidth = 100, insertwidth = 40, bg = 'black', justify = 'right')
        AffichageCalcul1.grid(row = 2, column = 1, columnspan = 5)

        #Ligne possédant un bug historique, un caractère fantôme reste présent sans que l'on comprenne pourquoi
        """button_inverse = Button(padx = 16, pady = 16, bd = 0, fg = '#c8c8c8', font = ('arial', 16, 'bold'), text = '1/​x', bg = 'black', activeforeground = "#727272", activebackground = "#292929", command lambda"e"""

        button_inverse = Button(padx = 16, pady = 16, bd = 0, fg = '#c8c8c8', font = ('arial', 16, 'bold'), text = '1/x', bg = 'black', activeforeground = "#727272", activebackground = "#292929", command = lambda:compilateur("&"))
        button_inverse.grid(row = 3, column = 4)
        button_pi = Button(padx = 16, pady = 16, bd = 0, fg = '#c8c8c8', font = ('arial', 19), text = 'π', bg = 'black', activeforeground = "#727272", activebackground = "#292929", command = lambda:compilateur("π"))
        button_pi.grid(row = 3, column = 3)
        button_racinecarre = Button(padx = 16, pady = 16, bd = 0, fg = '#c8c8c8', font = ('arial', 20, 'bold'), text = '√', bg = 'black', activeforeground = "#727272", activebackground = "#292929", command = lambda:racinecarre())
        button_racinecarre.grid(row = 3, column = 2)
        button_factorielle = Button(padx = 16, pady = 20, bd = 0, fg = '#c8c8c8', font = ('arial', 15, 'bold'), text = 'X!', bg = 'black', activeforeground = "#727272", activebackground = "#292929", command = lambda:compilateur("!"))
        button_factorielle.grid(row = 3, column = 0)
        button_posneg = Button(padx = 16, pady = 20, bd = 0, fg = '#c8c8c8', font = ('arial', 15, 'bold'), text = '±', bg = 'black', activeforeground = "#727272", activebackground = "#292929", command = lambda:positifnegatif())
        button_posneg.grid(row = 4, column = 0)
        button_carre = Button(padx = 16, pady = 16, bd = 0, fg = '#c8c8c8', font = ('arial', 20, 'bold'), text = 'X²', bg = 'black', activeforeground = "#727272", activebackground = "#292929", command = lambda:compilateur("²"))
        button_carre.grid(row = 5, column = 0)
        button_exposant = Button(padx = 16, pady = 16, bd = 0, fg = '#c8c8c8', font = ('arial', 20, 'bold'), text = 'Xʸ', bg = 'black', activeforeground = "#727272", activebackground = "#292929", command = lambda:compilateur("^"))
        button_exposant.grid(row = 3, column = 1)
        button_delta = Button(padx = 16, pady = 16, bd = 0, fg = '#c8c8c8', font = ('arial', 20, 'bold'), text = '△', bg = 'black', activeforeground = "#727272", activebackground = "#292929", command = lambda:delta())
        button_delta.grid(row = 6, column = 0)
        button_menu = Button(padx = 16, pady = 16, bd = 0, fg = '#c8c8c8', font = ('arial', 20, 'bold'), text = '↔', bg = 'black', activeforeground = "#727272", activebackground = "#292929", command = lambda:switch())
        button_menu.grid(row = 7, column = 0)


        button_exponentielle = Button(padx = 16, pady = 20, bd = 0, fg = 'white', font = ('arial', 20, 'bold'), text = 'e', bg = 'black', activeforeground = "#727272", activebackground = "#292929", command = lambda:compilateur("e"))
        button_exponentielle.grid(row = 8, column = 1)

        button_7 = Button(padx = 16, pady = 16, bd = 0, fg = 'white', font = ('arial', 20, 'bold'), text = '7', bg = 'black', activeforeground = "white", activebackground = "#292929", command = lambda:compilateur(7))
        button_7.grid(row = 5, column = 1)
        button_8 = Button(padx = 16, pady = 16, bd = 0, fg = 'white', font = ('arial', 20, 'bold'), text = '8', bg = 'black', activeforeground = "white", activebackground = "#292929", command = lambda:compilateur(8))
        button_8.grid(row = 5, column = 2)
        button_9 = Button(padx = 16, pady = 16, bd = 0, fg = 'white', font = ('arial', 20, 'bold'), text = '9', bg = 'black', activeforeground = "white", activebackground = "#292929", command = lambda:compilateur(9))
        button_9.grid(row = 5, column = 3)
        button_4 = Button(padx = 16, pady = 16, bd = 0, fg = 'white', font = ('arial', 20, 'bold'), text = '4', bg = 'black', activeforeground = "white", activebackground = "#292929", command = lambda:compilateur(4))
        button_4.grid(row = 6, column = 1)
        button_5 = Button(padx = 16, pady = 16, bd = 0, fg = 'white', font = ('arial', 20, 'bold'), text = '5', bg = 'black', activeforeground = "white", activebackground = "#292929", command = lambda:compilateur(5))
        button_5.grid(row = 6, column = 2)
        button_6 = Button(padx = 16, pady = 16, bd = 0, fg = 'white', font = ('arial', 20, 'bold'), text = '6', bg = 'black', activeforeground = "white", activebackground = "#292929", command = lambda:compilateur(6))
        button_6.grid(row = 6, column = 3)
        button_1 = Button(padx = 16, pady = 16, bd = 0, fg = 'white', font = ('arial', 20, 'bold'), text = '1', bg = 'black', activeforeground = "white", activebackground = "#292929", command = lambda:compilateur(1))
        button_1.grid(row = 7, column = 1)
        button_2 = Button(padx = 16, pady = 16, bd = 0, fg = 'white', font = ('arial', 20, 'bold'), text = '2', bg = 'black', activeforeground = "white", activebackground = "#292929", command = lambda:compilateur(2))
        button_2.grid(row = 7, column = 2)
        button_3 = Button(padx = 16, pady = 16, bd = 0, fg = 'white', font = ('arial', 20, 'bold'), text = '3', bg = 'black', activeforeground = "white", activebackground = "#292929", command = lambda:compilateur(3))
        button_3.grid(row = 7, column = 3)
        button_0 = Button(padx = 16, pady = 16, bd = 0, fg = 'white', font = ('arial', 20, 'bold'), text = '0', bg = 'black', activeforeground = "white", activebackground = "#292929", command = lambda:compilateur(0))
        button_0.grid(row = 8, column = 2)

        button_switch = Button(padx = 16, pady = 16, bd = 0, fg = '#ff7837', font = ('arial', 20, 'bold'), text = '¤', bg = 'black', activeforeground = "#ff7837", activebackground = "#292929", command = lambda:changement())
        button_switch.grid(row = 8, column = 0)
        button_egal = Button(padx = 16, pady = 16, bd = 0, fg = 'white', font = ('arial', 20, 'bold'), text = '=', bg = '#ff7837', activeforeground = "white", activebackground = "#ff7837", command = lambda:calculpologne())
        button_egal.grid(row = 8, column = 4)
        button_clear = Button(padx = 16, pady = 16, bd = 0, fg = '#ff7837', font = ('arial', 19, 'bold'), text = 'C', bg = 'black', activeforeground = "#ff7837", activebackground = "#292929", command = lambda:clear_pile())
        button_clear.grid(row = 4, column = 1)
        button_pourcentage = Button(padx = 16, pady = 16, bd = 0, fg = '#ff7837', font = ('arial', 18, 'bold'), text = '%', bg = 'black', activeforeground = "#ff7837", activebackground = "#292929", command = lambda:pourcentage(ecrit))
        button_pourcentage.grid(row = 4, column = 3)
        button_suppr = Button(padx = 16, pady = 20, bd = 0, fg = '#ff7837', font = ('arial', 15, 'bold'), text = 'DEL', bg = 'black', activeforeground = "#ff7837", activebackground = "#292929", command = lambda:delete())
        button_suppr.grid(row = 4, column = 2)
        button_virgule = Button(padx = 18, pady = 16, bd = 0, fg = 'white', font = ('arial', 20, 'bold'), text = ',', bg = 'black', activeforeground = "white", activebackground = "#292929", command = lambda:compilateur("."))
        button_virgule.grid(row = 8, column = 3)
        button_diviser = Button(padx = 18, pady = 11, bd = 0, fg = '#ff7837', font = ('arial', 21, 'bold'), text = '÷', bg = 'black', activeforeground = "#ff7837", activebackground = "#292929", command = lambda:compilateur("/"))
        button_diviser.grid(row = 4, column = 4)
        button_multiplier = Button(padx = 16, pady = 16, bd = 0, fg = '#ff7837', font = ('arial', 20, 'bold'), text = 'x', bg = 'black', activeforeground = "#ff7837", activebackground = "#292929", command = lambda:compilateur("x"))
        button_multiplier.grid(row = 5, column = 4)
        button_soustraire = Button(padx = 20, pady = 16, bd = 0, fg = '#ff7837', font = ('arial', 20, 'bold'), text = '–', bg = 'black', activeforeground = "#ff7837", activebackground = "#292929", command = lambda:compilateur("–"))
        button_soustraire.grid(row = 6, column = 4)
        button_additionner = Button(padx = 16, pady = 16, bd = 0, fg = '#ff7837', font = ('arial', 20, 'bold'), text = '+', bg = 'black', activeforeground = "#ff7837", activebackground = "#292929", command = lambda:compilateur("+"))
        button_additionner.grid(row = 7, column = 4)

        width = 296
        height = 492
        for i in range(9): #Boucle permettant d'agrandir la fenêtre de façon fluide
            width += 7
            height += 8
            fen.geometry(str(width) + "x" + str(height))
            fen.update()
        width += 21
        height += 15
        fen.geometry(str(width) + "x" + str(height))
        fen.update()
    else :


        button_7.destroy()
        button_8.destroy()
        button_9.destroy()
        button_4.destroy()
        button_5.destroy()
        button_6.destroy()
        button_1.destroy()
        button_2.destroy()
        button_3.destroy()
        button_0.destroy()

        button_switch.destroy()
        button_egal.destroy()
        button_clear.destroy()
        button_pourcentage.destroy()
        button_suppr.destroy()
        button_virgule.destroy()
        button_diviser.destroy()
        button_multiplier.destroy()
        button_soustraire.destroy()
        button_additionner.destroy()

        AffichageCalcul3.destroy()
        AffichageCalcul2.destroy()
        AffichageCalcul1.destroy()

        button_inverse.destroy()
        button_pi.destroy()
        button_racinecarre.destroy()
        button_posneg.destroy()
        button_carre.destroy()
        button_exposant.destroy()
        button_menu.destroy()
        button_delta.destroy()
        button_exponentielle.destroy()

        AffichageCalcul3 = Entry(font = ('arial', 20, 'bold'), fg = 'white', readonlybackground = 'black', state = 'readonly', bd = 0, selectborderwidth = 100, insertwidth = 40, bg = 'black', justify = 'right')
        AffichageCalcul3.grid(row = 0, column = 0, columnspan = 4)
        AffichageCalcul2 = Entry(font = ('arial', 16, 'bold'), fg = 'gray', readonlybackground = 'black', state = 'readonly', textvariable = anc, bd = 0, selectborderwidth = 100, insertwidth = 40, bg = 'black', justify = 'right')
        AffichageCalcul2.grid(row = 1, column = 0, columnspan = 4)
        AffichageCalcul1 = Entry(font = ('arial', 16, 'bold'), fg = 'white', readonlybackground = 'black', state = 'readonly', textvariable = text, bd = 0, selectborderwidth = 100, insertwidth = 40, bg = 'black', justify = 'right')
        AffichageCalcul1.grid(row = 2, column = 0, columnspan = 4)

        button_7 = Button(padx = 16, pady = 16, bd = 0, fg = 'white', font = ('arial', 20, 'bold'), text = '7', bg = 'black', activeforeground = "white", activebackground = "#292929", command = lambda:compilateur(7))
        button_7.grid(row = 4, column = 0)
        button_8 = Button(padx = 16, pady = 16, bd = 0, fg = 'white', font = ('arial', 20, 'bold'), text = '8', bg = 'black', activeforeground = "white", activebackground = "#292929", command = lambda:compilateur(8))
        button_8.grid(row = 4, column = 1)
        button_9 = Button(padx = 16, pady = 16, bd = 0, fg = 'white', font = ('arial', 20, 'bold'), text = '9', bg = 'black', activeforeground = "white", activebackground = "#292929", command = lambda:compilateur(9))
        button_9.grid(row = 4, column = 2)
        button_4 = Button(padx = 16, pady = 16, bd = 0, fg = 'white', font = ('arial', 20, 'bold'), text = '4', bg = 'black', activeforeground = "white", activebackground = "#292929", command = lambda:compilateur(4))
        button_4.grid(row = 5, column = 0)
        button_5 = Button(padx = 16, pady = 16, bd = 0, fg = 'white', font = ('arial', 20, 'bold'), text = '5', bg = 'black', activeforeground = "white", activebackground = "#292929", command = lambda:compilateur(5))
        button_5.grid(row = 5, column = 1)
        button_6 = Button(padx = 16, pady = 16, bd = 0, fg = 'white', font = ('arial', 20, 'bold'), text = '6', bg = 'black', activeforeground = "white", activebackground = "#292929", command = lambda:compilateur(6))
        button_6.grid(row = 5, column = 2)
        button_1 = Button(padx = 16, pady = 16, bd = 0, fg = 'white', font = ('arial', 20, 'bold'), text = '1', bg = 'black', activeforeground = "white", activebackground = "#292929", command = lambda:compilateur(1))
        button_1.grid(row = 6, column = 0)
        button_2 = Button(padx = 16, pady = 16, bd = 0, fg = 'white', font = ('arial', 20, 'bold'), text = '2', bg = 'black', activeforeground = "white", activebackground = "#292929", command = lambda:compilateur(2))
        button_2.grid(row = 6, column = 1)
        button_3 = Button(padx = 16, pady = 16, bd = 0, fg = 'white', font = ('arial', 20, 'bold'), text = '3', bg = 'black', activeforeground = "white", activebackground = "#292929", command = lambda:compilateur(3))
        button_3.grid(row = 6, column = 2)
        button_0 = Button(padx = 16, pady = 16, bd = 0, fg = 'white', font = ('arial', 20, 'bold'), text = '0', bg = 'black', activeforeground = "white", activebackground = "#292929", command = lambda:compilateur(0))
        button_0.grid(row = 7, column = 1)

        button_switch = Button(padx = 16, pady = 16, bd = 0, fg = '#ff7837', font = ('arial', 20, 'bold'), text = '¤', bg = 'black', activeforeground = "#ff7837", activebackground = "#292929", command = lambda:changement())
        button_switch.grid(row = 7, column = 0)
        button_egal = Button(padx = 16, pady = 16, bd = 0, fg = 'white', font = ('arial', 20, 'bold'), text = '=', bg = '#ff7837', activeforeground = "white", activebackground = "#ff7837", command = lambda:calculpologne())
        button_egal.grid(row = 7, column = 3)
        button_clear = Button(padx = 16, pady = 16, bd = 0, fg = '#ff7837', font = ('arial', 19, 'bold'), text = 'C', bg = 'black', activeforeground = "#ff7837", activebackground = "#292929", command = lambda:clear_pile())
        button_clear.grid(row = 3, column = 0)
        button_pourcentage = Button(padx = 16, pady = 16, bd = 0, fg = '#ff7837', font = ('arial', 18, 'bold'), text = '%', bg = 'black', activeforeground = "#ff7837", activebackground = "#292929", command = lambda:pourcentage(ecrit))
        button_pourcentage.grid(row = 3, column = 2)
        button_suppr = Button(padx = 16, pady = 20, bd = 0, fg = '#ff7837', font = ('arial', 15, 'bold'), text = 'DEL', bg = 'black', activeforeground = "#ff7837", activebackground = "#292929", command = lambda:delete())
        button_suppr.grid(row = 3, column = 1)
        button_virgule = Button(padx = 18, pady = 16, bd = 0, fg = 'white', font = ('arial', 20, 'bold'), text = ',', bg = 'black', activeforeground = "white", activebackground = "#292929", command = lambda:compilateur("."))
        button_virgule.grid(row = 7, column = 2)
        button_diviser = Button(padx = 18, pady = 11, bd = 0, fg = '#ff7837', font = ('arial', 21, 'bold'), text = '÷', bg = 'black', activeforeground = "#ff7837", activebackground = "#292929", command = lambda:compilateur("/"))
        button_diviser.grid(row = 3, column = 3)
        button_multiplier = Button(padx = 16, pady = 16, bd = 0, fg = '#ff7837', font = ('arial', 20, 'bold'), text = 'x', bg = 'black', activeforeground = "#ff7837", activebackground = "#292929", command = lambda:compilateur("x"))
        button_multiplier.grid(row = 4, column = 3)
        button_soustraire = Button(padx = 20, pady = 16, bd = 0, fg = '#ff7837', font = ('arial', 20, 'bold'), text = '–', bg = 'black', activeforeground = "#ff7837", activebackground = "#292929", command = lambda:compilateur("–"))
        button_soustraire.grid(row = 5, column = 3)
        button_additionner = Button(padx = 16, pady = 16, bd = 0, fg = '#ff7837', font = ('arial', 20, 'bold'), text = '+', bg = 'black', activeforeground = "#ff7837", activebackground = "#292929", command = lambda:compilateur("+"))
        button_additionner.grid(row = 6, column = 3)




        width = 380
        height = 579
        for i in range(9): #Boucle permettant de rétrécir la fenêtre de façon fluide
            width -= 7
            height -= 8
            fen.geometry(str(width) + "x" + str(height))
            fen.update()
        width -= 21
        height -= 15
        fen.geometry(str(width) + "x" + str(height))
        fen.update()


def clear_pile():
    """
    La fonction clear_pile ne prend aucun paramètre.
    Elle permet de vider la pile contenant le calcul à réaliser.
    Elle renvoit une chaine de caractère vide.
    """
    global ecrit, ancien, memoireinverse
    if "&" in ecrit :
        ancien = memoireinverse
    else :
        ancien = ecrit
    anc.set(ancien)
    while calcul.est_vide() != True :
        calcul.depiler()
    text.set("0")
    ecrit = ""
    return ecrit


def racinecarre():
    """
    La fonction racinecarre ne prend aucun paramètre. Elle permet de rajouter
    la chaine de caractère √ devant le nombre dont l'utilisateur veut sa racine carré.
    Elle renvoit une chaine de caractère.
    """
    global nb, ecrit
    if len(calcul.lst) > 0:
        nb = calcul.sommet()
        if type(nb) != str:
            memoire = ecrit[-1]
            ecrit = ecrit[:-1]
            ecrit = ecrit + "√" + memoire
            text.set(ecrit)
            calcul.depiler()
            calcul.empiler(sqrt(nb))


def close_window():
    """
    La fonction close_window ne prend aucun paramètre,
    elle permet de quitter la fenêtre tkinter
    """
    fen.destroy()

def compilateur(n):
    """
    La fonction compilateur qui a pour paramètre n, sert à mettre dans la pile les
    chiffres/signes demandés, en les mettant à virgule si demandé mais crée également
    un tableau à empiler pour les exposants et carré, la fonction empile également
    l'exponentielle, pi et prépare la factorielle, elle sert également pour calcul normal.
    """
    global ecrit, text, memoireinverse
    neg = 0

    if global_var == 0:
        return

    if n == ".":
        var = calcul.depiler()
        ecrit = ecrit + "."
        text.set(ecrit)
        if type(var) == list and len(var) == 3:
            var[2] = str(var[2]) + "."
            calcul.empiler(var)
            return
        else:
            calcul.empiler(str(var) + ".")
            return

    elif len(calcul.lst) > 0:
        var = calcul.depiler()
        if n == "&":
            if type(var) != str:
                calcul.empiler([var, "^", -1])
                memoireinverse = ecrit + "^-1"
                text.set(memoireinverse)
                ecrit = ecrit + "&"
                return
            else:
                calcul.empiler(var)
        if type(var) == list and len(var) == 2:
            var.append(n)
            calcul.empiler(var)
            ecrit = ecrit + str(n)
            text.set(ecrit)
            return
        elif n == "²":
            calcul.empiler([var, "^", 2])
            ecrit = ecrit + n
            text.set(ecrit)
            return
        if str(ecrit[-1]) == ".":
            if type(var) == list and len(var) == 3:
                var[2] = float(str(var[2]) + str(n))
                calcul.empiler(var)
                ecrit = ecrit +str(n)
                text.set(ecrit)
                return
            if type(n) == str:
                var = var[:-1]
                calcul.empiler(int(var))
                calcul.empiler(n)
            calcul.empiler(float(var + str(n)))
            ecrit = ecrit + str(n)
            text.set(ecrit)
            return

        calcul.empiler(var)




        if n == "^":
            calcul.empiler([calcul.depiler(), "^"])
            ecrit = ecrit + "^"
            text.set(ecrit)
            return

        if n == "!":
            calcul.empiler(str(calcul.depiler()) + "!")
            ecrit = ecrit + "!"
            text.set(ecrit)
            return

        if n == 'x' or n == '–' or n == '/' or n == '+':
            calcul.empiler(n)
            ecrit = ecrit + str(n)
            text.set(ecrit)
            return

    if n == "e":
        calcul.empiler(exp(1))
        ecrit = ecrit + n
        text.set(ecrit)
        return

    if n == "π":
        calcul.empiler(pi)
        ecrit = ecrit + "π"
        text.set(ecrit)
        return

    if type(n) == int:
        calcul.empiler(n)
        ecrit = ecrit + str(n)
        text.set(ecrit)
        return


def pourcentage(pourc):
    """
    La fonction pourcentage prend en parametre une chaine de caractère pourc.
    Elle permet de transformer la chaine de caractère entrée en pourcentage. Elle renvoit une chaine de caractère
    """
    global ecrit
    result = float(pourc)
    result = result / 100
    ecrit = str(result)
    text.set(str(result))
    for i in range(len(calcul.lst)):
        calcul.depiler()
    calcul.empiler(result)
    return

def positifnegatif():
    """
    La fonction positifnegatif ne prend aucun paramètre. Elle permet de transformer le calcul en son opposé.
    Elle renvoit une chaine de caractère contenant l'opposé du calcul.
    """
    global ecrit, calcul
    if len(calcul.lst) > 0:
        n = calcul.depiler()
        if type(n) != str:
            j = -len(str(n))
            if type(n) == str:
                calcul.empiler(n)
                return
            if str(n)[0] == "-":
                n = -n
                ecrit = ecrit[:j] + str(n)
                text.set(ecrit)
            else:
                n = -n
                ecrit = ecrit[:j] + str(n)
                text.set(ecrit)
            calcul.empiler(n)
            return ecrit
        else:
            calcul.empiler(n)


def delete():
    """
    La fonction delete ne prend aucun paramètre. Elle permet à l'utilisateur de supprimer
    sa / ses dernières actions. Elle renvoit une chaine de caractère ne contenant pas le caractère supprimé,
    elle vérifie si le nombre est à virgule ou non pour mettreun nouveau chiffre après la virgule et
    si il y a un exposant ou une factorielle
    """
    global calcul, ecrit
    if len(calcul.lst) == 0:
        return
    for j in ecrit:
        if j == "=":
            clear_pile()
            ecrit = ""
            text.set("0")
            return
    var = calcul.depiler()
    if ecrit[-1] == "²":
        ecrit = ecrit[:-1]
        text.set(ecrit)
        calcul.empiler(var[0])
        return
    if type(var) == list: #vérifier si c'est une liste, dans ce cas ce serait un exposant
        ecrit = ecrit[:-1]
        text.set(ecrit)
        if len(var) == 2:
            calcul.empiler(var[0])
            return
        if str(var[2])[-1] == ".": #vérifier si le nombre est à virgule ou non quand il est en exposant (donc dans un tableau)
            var[2] = str(var[2])[:-1]
            calcul.empiler(var)
            return
        if len(str(var[2])) > 1 and str(var[2])[-2] == ".": #vérifier si le nombre à virgule de l'exposant a dejà perdu son nombre ou pas (ex : 2. tout cours ou non)
            var[2] = str(var[2])[:-1]
            calcul.empiler(var)
            return
        var = var[:-1]
        calcul.empiler(var)
        return
    if type(var) == float:
        var = str(var)[:-1]
        ecrit = ecrit[:-1]
        text.set(ecrit)
        calcul.empiler(var)
        return
    if type(var) == str and var[-1] == ".":
        var = int(var[:-1])
        ecrit = ecrit[:-1]
        text.set(ecrit)
        calcul.empiler(var)
        return


    calcul.empiler(var)
    if ecrit[-1] == "!":
        ecrit = ecrit[:-1]
        text.set(ecrit)
        calcul.empiler(calcul.depiler()[:-1])
        return
    calcul.depiler()
    if calcul.est_vide() == True:
        ecrit = ""
        text.set("0")
        return
    ecrit = ecrit[:-1]
    if ecrit == "-" or ecrit == "":
        text.set(0)
        ecrit = ""
        return
    text.set(ecrit)
    return

def secret(event):
    """
    C'est secret !!!
    """
    im = Image.open("QRcode.png")
    im.show()

def carre():
    """
    La fonction carre ne prend aucun paramètre. Elle permet de calculer le carré
    d'un nombre. Elle renvoit un tableau sous la forme [nombre de base, "^", 2]
    comme pour les exposants et rajoute ² dans ecrit.
    """
    global nb, ecrit
    nb = calcul.sommet() #On récupère le dernier nombre entré par l'utilisateur grâce à la méthode .sommet()
    ecrit = ecrit + "²"
    text.set(ecrit)
    calcul.empiler(nb)
    calcul.empiler('x')

def factorielle(x):
    """
    La fonction factorielle prend un paramètre une chaine de caractère x.
    Elle permet de calculer la factorielle d'un nombre. Elle renvoit le
    resultat de la factorielle
    """
    global calcul, ecrit
    neg = 0
    if x[0] == "-": #On regarde si on doit faire la factorielle d'un nombre négatif
        x = x[1:] #On retire le "-" pour pouvoir calculer la factorielle
        if int(x)%2 == 1 : #Condition pour savoir si le résultat de la factorielle doit être positif ou négatif
            neg = 1
    if x.isnumeric() == True: #La méthode .isnumeric() permet de vérifier si un nombre est transformable en entier
        if neg == 1:
            x = "-" + x
            nbr = int(x)
            for i in range(1, -nbr):
                nbr = nbr * i
        else:
            nbr = int(x)
            for i in range(1, nbr):
                nbr = nbr * i
        return nbr


def raccourci(event):
    """
    La fonction raccourci ne prend aucun paramètre. Elle permet à l'utilisateur
    d'utiliser la calculatrice avec les touches de son clavier.
    Elle renvoit la touche utilisé par l'utilisateur.
    """
    tabsign = ['*', '-', '+', '/', '.']
    var = event.char
    if event.keysym == "Delete":
        clear_pile()
    if var == '\x08' : #\x08 correspond à la touche "supprimer" du clavier
        delete()
    if var == '\r' : #\r correspond à la touche "entré" du clavier
        calculpologne()
    if var == '²':
        carre()
        return
    if var == '%':
        pourcentage(ecrit)
    if var in tabsign or var == '*' or var == '–':
        if var == '*':
            compilateur('x')
            return
        if var == '-':
            compilateur('–')
            return
        compilateur(var)
    if var.isnumeric() == True: #On vérifie si la touche sur laquelle à appuyé l'utilisateur est un entier
        compilateur(int(var))
    return

def Delta(a, b, c):
   """
   La fonction Delta prend en paramètre trois entiers a, b et c.
   Elle permet de trouver delta. Elle renvoie delta.
   """
   return b*b - 4*a*c #Calcul de delta

def solv(a, b, c):
   """
   La fonction solv prend en paramètre trois entiers a, b et c.
   Elle permet de résoudre les équations pour trouver les racines d'une
    équation du second degré. Elle renvoie les racines si il y en a.
    """
   global deltasolv, ecrit
   anc.set(ecrit)
   delta = Delta(int(a), int(b), int(c))
   if delta > 0:
      racineDeDelta = sqrt(delta)
      retour = [round((-int(b) - racineDeDelta) / (2 * int(a)), 2), round((-int(b) + racineDeDelta) / (2 * int(a)), 2)] #Calcul des racines de delta
      racine = "X₁ = " + str(retour[0]) + " et X₂ = " + str(retour[1])
   elif delta < 0:
      retour = []
      racine = "Aucune solution réelle"
   else:
      retour = [-int(b) / (2 * int(a))] #Calcul racine de delta
      racine = "X = " + str(retour[0])
   ecrit = racine
   text.set(ecrit)
   deltasolv = 0
   return

def delta ():
    """
    La fonction delta ne prend aucun paramètre. Elle permet de récuperer
    les entiers a, b, c afin de trouver les racines d'une équation du
    second degré. Elle ne renvoit rien.
    """
    global a, b, c, ecrit, deltasolv, calcul
    if len(calcul.lst) == 3:
        for i in calcul.lst:
            if type(i) == str:
                return
        tot = 0
        for i in ecrit :
            calcul.empiler(str(i))
        c = calcul.depiler()
        b = calcul.depiler()
        a = calcul.depiler()
        ecrit = str(a)+ "X² + "+ str(b) + "X + " + str(c)
        text.set(ecrit)
        deltasolv = 1

def switch():
    """
    La fonction switch ne prend aucun paramètre.
    Elle permet de changer le mode de la calculatrice :
        0 : Notation polonaise inversée
        1 : Notation classique
        Elle renvoie la nouvelle valeure de chang.
    """
    global chang
    if chang == 0 :
        chang = 1
        print("Passage en mode normal")
        return chang
    if chang == 1 :
        chang = 0
        print("Passage en mode Pologne")
        return chang


def snake (event):
    """
    La fonction snake ne prend aucun paramètre et est lancée quand les touches
    's', 'n', 'a', 'k' et 'e' sont pressées à la suite, elle permet donc de
    jouer au jeu snake.
    """
    global fen, flag, Serpent, pX, pY, direction, pomme, lancement
    flag = 0
    lancement = 0
    fen.destroy()
    fen = Tk()
    fen.config(bg='Black')
    def move():
        global x, y, pX, pY, Serpent
        can.delete('all')
        i = len(Serpent) - 1
        j = 0
        while i > 0:
            Serpent[i][0] = Serpent[i-1][0]
            Serpent[i][1] = Serpent[i-1][1]
            can.create_oval(Serpent[i][0], Serpent[i][1], Serpent[i][0] + 10, Serpent[i][1] + 10, outline = 'white', fill = 'black')
            i = i - 1


        can.create_rectangle(pX, pY, pX + 5, pY + 5, outline = 'Red', fill = 'black')

        if direction  == 'gauche':
            Serpent[0][0]  = Serpent[0][0] - dx
            if Serpent[0][0] < 0:
                return  gameover()
        elif direction  == 'droite':
            Serpent[0][0]  = Serpent[0][0] + dx
            if Serpent[0][0] > 500:
                return  gameover()
        elif direction  == 'haut':
            Serpent[0][1]  = Serpent[0][1] - dy
            if Serpent[0][1] < 0:
                return  gameover()
        elif direction  == 'bas':
            Serpent[0][1]  = Serpent[0][1] + dy
            if Serpent[0][1] > 500:
                return  gameover()
        can.create_oval(Serpent[0][0], Serpent[0][1], Serpent[0][0]+10, Serpent[0][1]+10, outline='white', fill='blue')
        test()
        test()

        if flag != 0:
            fen.after(60, move)

    def newGame():
        global pX, pY, flag, lancement
        if lancement >= 1:
            return snake("a")
        lancement = lancement + 1
        if flag == 0:
            flag = 1
        move()

    def left(event):
        global direction
        direction = 'gauche'

    def right(event):
        global direction
        direction = 'droite'

    def up(event):
        global direction
        direction = 'haut'

    def down(event):
        global direction
        direction = 'bas'

    def test():
        global pomme, x, y, pX, pY, Serpent

        for j in range(1, len(Serpent)):
            if Serpent[0][0] == Serpent[j][0] and Serpent[0][1] == Serpent[j][1]:

                return gameover()

        if Serpent[1][0] > pX - 10 and  Serpent[1][0] < pX + 10:
            if Serpent[1][1] > pY - 10 and Serpent[1][1] < pY + 10:
                #On remet une pomme au hasard
                pX = randrange(5, 495)
                pY = randrange(5, 495)
                can.coords(pomme, pX, pY, pX+5, pY+5)
                #On joute un nouveau point au serpent
                Serpent.append([0, 0])

    def gameover():
        time.sleep(0.5)
        return snake("a")

    x = 250
    y = 250
    dx, dy = 10, 10
    direction = 'haut'
    Serpent=[[x, y], [x + 2.5, y + 2.5], [x + 5, y + 5], [0, 0]]

    pX = randrange(5, 495)
    pY = randrange(5, 495)
    can = Canvas(fen, width = 500, height = 500, bg = 'black')
    can.grid(ipadx = 5, ipady = 5)

    oval1 = can.create_oval(Serpent[1][0], Serpent[1][1], Serpent[1][0] + 10, Serpent[1][1] + 10, outline = 'white', fill = 'red')

    oval = can.create_oval(Serpent[0][0], Serpent[0][1], Serpent[0][0] + 10, Serpent[0][1] + 10, outline = 'white', fill = 'white')

    pomme = can.create_rectangle(pX, pY, pX + 5, pY + 5, outline='Red', fill='black')

    b1 = Button(fen, text = 'Lancer', command = newGame, bg  ='black' , fg = 'white')
    b1.grid(ipadx = 5, ipady = 5)

    b2 = Button(fen, text = 'Quitter', command = fen.destroy, bg = 'black' , fg = 'white')
    b2.grid(ipadx = 5, ipady = 5)

    tex1 = Label(fen, text = "Cliquez sur 'Lancer' pour commencer le jeu.", bg = 'White' , fg = 'Black')
    tex1.grid(ipadx = 0, ipady = 11)

    fen.bind('<d>', right)
    fen.bind('<q>', left)
    fen.bind('<z>' , up)
    fen.bind('<s>', down)

    fen.bind('<Right>', right)
    fen.bind('<Left>', left)
    fen.bind('<Up>' , up)
    fen.bind('<Down>', down)
    fen.geometry("514x630")

    fen.update()

# ======= Initialisation fenêtre tkinter et principales variables ======= #

ecrit = ""
ancien = ""
fen = Tk() # Création de la fenêtre TKinter
fen.config(cursor = "wait")
fen.title('Calculatrice')
fen.config(bg = "#000000") # On définit la couleur du fond de la fenêtre Tkinter
fen.protocol("WM_DELETE_WINDOW",lambda : close_window()) # On lance la fonction close_window() si on appuie sur la croix rouge en haut à droite pour fermer la fenêtre
fen.geometry('296x492')
fen.focus_force()
calcul = Pile()
global_var = 0
chang = 0
extend = 1
deltasolv = 0
anc = StringVar()
anc.set(ancien)
text = StringVar()
text.set("0")
global_var = 1

# ======= Affichage ======= #

AffichageCalcul3 = Entry(font = ('arial', 20, 'bold'), fg = 'white', readonlybackground = 'black', state = 'readonly', bd = 0, selectborderwidth = 100, insertwidth = 40, bg = 'black', justify = 'right')
AffichageCalcul3.grid(columnspan = 4)
AffichageCalcul2 = Entry(font = ('arial', 16, 'bold'), fg = 'gray', readonlybackground = 'black', state = 'readonly', textvariable = anc, bd = 0, selectborderwidth = 100, insertwidth = 40, bg = 'black', justify = 'right')
AffichageCalcul2.grid(columnspan = 4)
AffichageCalcul1 = Entry(font = ('arial', 16, 'bold'), fg = 'white', readonlybackground = 'black', state = 'readonly', textvariable = text, bd = 0, selectborderwidth = 100, insertwidth = 40, bg = 'black', justify = 'right')
AffichageCalcul1.grid(columnspan = 4)

# ======= Initialisation des boutons principaux ======= #

button_7 = Button(padx = 16, pady = 16, bd = 0, fg = 'white', font = ('arial', 20, 'bold'), text = '7', bg = 'black', activeforeground = "white", activebackground = "#292929", command = lambda:compilateur(7))
button_7.grid(row = 4, column = 0)

button_8 = Button(padx = 16, pady = 16, bd = 0, fg = 'white', font = ('arial', 20, 'bold'), text = '8', bg = 'black', activeforeground = "white", activebackground = "#292929", command = lambda:compilateur(8))
button_8.grid(row = 4, column = 1)

button_9 = Button(padx = 16, pady = 16, bd = 0, fg = 'white', font = ('arial', 20, 'bold'), text = '9', bg = 'black', activeforeground = "white", activebackground = "#292929", command = lambda:compilateur(9))
button_9.grid(row = 4, column = 2)

button_4 = Button(padx = 16, pady = 16, bd = 0, fg = 'white', font = ('arial', 20, 'bold'), text = '4', bg = 'black', activeforeground = "white", activebackground = "#292929", command = lambda:compilateur(4))
button_4.grid(row = 5, column = 0)

button_5 = Button(padx = 16, pady = 16, bd = 0, fg = 'white', font = ('arial', 20, 'bold'), text = '5', bg = 'black', activeforeground = "white", activebackground = "#292929", command = lambda:compilateur(5))
button_5.grid(row = 5, column = 1)

button_6 = Button(padx = 16, pady = 16, bd = 0, fg = 'white', font = ('arial', 20, 'bold'), text = '6', bg = 'black', activeforeground = "white", activebackground = "#292929", command = lambda:compilateur(6))
button_6.grid(row = 5, column = 2)

button_1 = Button(padx = 16, pady = 16, bd = 0, fg = 'white', font = ('arial', 20, 'bold'), text = '1', bg = 'black', activeforeground = "white", activebackground = "#292929", command = lambda:compilateur(1))
button_1.grid(row = 6, column = 0)

button_2 = Button(padx = 16, pady = 16, bd = 0, fg = 'white', font = ('arial', 20, 'bold'), text = '2', bg = 'black', activeforeground = "white", activebackground = "#292929", command = lambda:compilateur(2))
button_2.grid(row = 6, column = 1)

button_3 = Button(padx = 16, pady = 16, bd = 0, fg = 'white', font = ('arial', 20, 'bold'), text = '3', bg = 'black', activeforeground = "white", activebackground = "#292929", command = lambda:compilateur(3))
button_3.grid(row = 6, column = 2)

button_0 = Button(padx = 16, pady = 16, bd = 0, fg = 'white', font = ('arial', 20, 'bold'), text = '0', bg = 'black', activeforeground = "white", activebackground = "#292929", command = lambda:compilateur(0))
button_0.grid(row = 7, column = 1)



button_switch = Button(padx = 16, pady = 16, bd = 0, fg = '#ff7837', font = ('arial', 20, 'bold'), text = '¤', bg = 'black', activeforeground = "#ff7837", activebackground = "#292929", command = lambda:changement())
button_switch.grid(row = 7, column = 0)

button_egal = Button(padx = 16, pady = 16, bd = 0, fg = 'white', font = ('arial', 20, 'bold'), text = '=', bg = '#ff7837', activeforeground = "white", activebackground = "#ff7837", command = lambda:calculpologne())
button_egal.grid(row = 7, column = 3)

button_clear = Button(padx = 16, pady = 16, bd = 0, fg = '#ff7837', font = ('arial', 19, 'bold'), text = 'C', bg = 'black', activeforeground = "#ff7837", activebackground = "#292929", command = lambda:clear_pile())
button_clear.grid(row = 3, column = 0)

button_pourcentage = Button(padx = 16, pady = 16, bd = 0, fg = '#ff7837', font = ('arial', 18, 'bold'), text = '%', bg = 'black', activeforeground = "#ff7837", activebackground = "#292929", command = lambda:pourcentage(ecrit))
button_pourcentage.grid(row = 3, column = 2)

button_suppr = Button(padx = 16, pady = 20, bd = 0, fg = '#ff7837', font = ('arial', 15, 'bold'), text = 'DEL', bg = 'black', activeforeground = "#ff7837", activebackground = "#292929", command = lambda:delete())
button_suppr.grid(row = 3, column = 1)

button_virgule = Button(padx = 18, pady = 16, bd = 0, fg = 'white', font = ('arial', 20, 'bold'), text = ',', bg = 'black', activeforeground = "white", activebackground = "#292929", command = lambda:compilateur("."))
button_virgule.grid(row = 7, column = 2)

button_diviser = Button(padx = 18, pady = 11, bd = 0, fg = '#ff7837', font = ('arial', 21, 'bold'), text = '÷', bg = 'black', activeforeground = "#ff7837", activebackground = "#292929", command = lambda:compilateur("/"))
button_diviser.grid(row = 3, column = 3)

button_multiplier = Button(padx = 16, pady = 16, bd = 0, fg = '#ff7837', font = ('arial', 20, 'bold'), text = 'x', bg = 'black', activeforeground = "#ff7837", activebackground = "#292929", command = lambda:compilateur("x"))
button_multiplier.grid(row = 4, column = 3)

button_soustraire = Button(padx = 20, pady = 16, bd = 0, fg = '#ff7837', font = ('arial', 20, 'bold'), text = '–', bg = 'black', activeforeground = "#ff7837", activebackground = "#292929", command = lambda:compilateur("–"))
button_soustraire.grid(row = 5, column = 3)

button_additionner = Button(padx = 16, pady = 16, bd = 0, fg = '#ff7837', font = ('arial', 20, 'bold'), text = '+', bg = 'black', activeforeground = "#ff7837", activebackground = "#292929", command = lambda:compilateur("+"))
button_additionner.grid(row = 6, column = 3)

def premiersnake(event):
    fen.bind("<n>", secondsnake)

def secondsnake(event):
    fen.bind("<a>", troissnake)

def troissnake(event):
    fen.bind("<k>", quatresnake)

def quatresnake(event):
    fen.bind("<e>", snake)

#======================


def secret1(event):
    fen.bind("<Up>", secret2)

def secret2(event):
    fen.bind("<Left>", secret3)

def secret3(event):
    fen.bind("<Down>", secret4)

def secret4(event):
    fen.bind("<Up>", secret5)

def secret5(event):
    fen.bind("<Right>", secret6)

def secret6(event):
    fen.bind("<Right>", secret)

fen.bind("<s>", premiersnake)
fen.bind("<Up>", secret1)
fen.bind("<Key>", raccourci)
fen.config(cursor = "")
fen.mainloop()