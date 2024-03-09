from random import randint
#5import corrige_pendu

#Question 0
#Compléter dans les chaînes ci-dessous, sans enlever les guillemets:
NOM = "OUHAIBIA"
PRENOM = "Mohamed Amine"
EMAIL = "mohamed-amine.ouhaibia@universite-paris-saclay.fr"


#Question 1
def charge_mots(chemin):
    lmax=0
    f = open(chemin)
    t = f.readlines()
    for i in range(len(t)):
        t[i] = t[i].strip()
        if len(t[i])> lmax:
            lmax = len(t[i])
    f.close()
    return (t,lmax)

#Question 2
def test_charge_mots():
    nbm , lmx = charge_mots("mots.txt")  #nbm: nombre de mots, lmx:longueur maximale
    assert(len(nbm)==59705)
    assert(lmx==25)
    assert(nbm[43570]== "poisson")
    assert(nbm[20956]== "embarrasser")
    return None

#Question 3
def mots_par_longueur(tab_mots, lmax):
    mpl= []            #mpl: mots par longueur
    for i in range(lmax+1):
        mpl.append([])
    for i in range(0, len(tab_mots)):
        mpl[len(tab_mots[i])]+=[tab_mots[i]]
    return mpl

#Question 4
def test_mots_par_longueur():
    print (mots_par_longueur(['a', 'bonbon', 'code', 'dos', 'etre'], 6))
    assert mots_par_longueur(['a', 'bonbon', 'code', 'dos', 'etre'], 6) == [[], ['a'], [], ['dos'], ['code', 'etre'], [], ['bonbon']]
    return None

           
#Question 5
def choix_mot(tab_mots_long, l):
    return tab_mots_long[l][randint(0, len(tab_mots_long[l])-1)]

#Question 6
def test_choix_mot():
    tab_mots, lmax = charge_mots("mots.txt")
    tab_mots_long = mots_par_longueur(tab_mots, lmax)
    assert choix_mot([[], ['a'], [], ['dos'], ['code', 'etre'],[], ['bonbon']], 1) == "a"
    assert choix_mot([[], ['a'], [], ['dos'], ['code', 'etre'],[], ['bonbon']], 3) == "dos"
    assert (choix_mot([[], ['a'], [], ['dos'], ['code', 'etre'],[], ['bonbon']], 4) in ("code","etre"))
    return

#Question 7
def init_probleme(mot):
    pb=[]
    for i in range(len(mot)):
           pb+= [(mot[i], False)]
    return pb

#Question 8
def test_init_probleme():
    assert init_probleme("bonjour") == [("b", False),("o", False),("n", False),("j", False),("o", False),("u", False),("r", False)]
    return None

#Question 9
def num_inconnues (probleme):
    lnt=0
    for i in range(len(probleme)):
           if not probleme[i][1]:
               lnt+=1
    return lnt
           
# Question 10
def test_num_inconnues():
    assert num_inconnues([("b", False),("o", False),("n", False),("j", False),("o", False),("u", False),("r", False)]) == 7
    assert num_inconnues([("u", False),("p",True),("s",True)]) == 1
    assert num_inconnues([("a", True),("z",True),("e",True)]) == 0
    return None

# Question 11
def joue(probleme, lettre):
    probleme2=[]
    for i in range(len(probleme)):
            if probleme[i][0]==lettre:
                probleme2+=[(probleme[i][0],True)]
            else:
                probleme2+=[probleme[i]]
    return probleme2

# Question 12
def test_joue():
    assert joue([("a",False),("z",True),("e",False)],"e") == [("a",False),("z",True),("e",True)]
    assert joue([("q",True),("s",True),("d",True)],"d")   == [("q",True),("s",True),("d",True)]
    assert joue([("p",False),("i",False),("i",False)],"i")== [("p",False),("i",True),("i",True)]
    return None

# Question 13
def affiche_probleme(probleme):
    m=""
    for i in range(len(probleme)):
        if probleme[i][1]:
            m+=probleme[i][0]
        else:
            m+="."
    print(m)

PENDU = (
    '  ___ ',
    ' |   |',
    ' o   |',
    '/|\  |',
    '/ \  |',
    '     |')

# Question 14
def affiche_pendu(n):
    k=0
    for i in range(len(PENDU)):
        for j in range(len(PENDU[i])):
            c=PENDU[i][j]
            if (c==" "):
                print(c,end="")
            elif (k < n):
                print(c, end='')
                k = k + 1
            else:
                print(" ", end='')
        print()

# Question 15
def partie(mot):
    probleme= init_probleme(mot)
    erreur=0
    while(erreur<15 and num_inconnues(probleme)!=0):
        affiche_probleme(probleme)
        lettre = str(input("Entrez une lettre entre a et z:"))
        if not ord("a")<=ord(lettre)<=ord("z"):
            lettre = str(input("La lettre n'est pas entre a et z, entrez une lettre valide:"))
        joue(probleme,lettre)
        if joue(probleme, lettre) == probleme:
            erreur+=1
        else:
            probleme=joue(probleme,lettre)
        affiche_pendu(erreur)
        if num_inconnues(probleme)==0:
            print("Bravo, tu es un as de l'orthographe, le mot était ", mot)
        if erreur==15:
            print("Perdu! Ouvre un dictionnaire frero, le mot était ", mot)

#### NE PAS MODIFIER LE CODE CI-DESSOUS

def jeu():
    mots, lmax = charge_mots("mots.txt")
    lmots = mots_par_longueur(mots, lmax)
    while True:
        s = input("Saisir une longueur de mot ou q pour quitter: ")
        if s == 'q':
            print ("Au revoir.")
            return
        try:
            l = int(s)
            if l > lmax or l <= 0:
                print ("Longueur invalide")
                continue
            mot = choix_mot(lmots, l)
            partie (mot)
        except ValueError:
            print ("Saisie invalide")



jeu()