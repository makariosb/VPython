# -*- coding: cp1253 -*-
from visual import *
def ellipsi():
    return ellipsoid(pos=(0,0,0), size=(1.5,1,1))

dict={"Βελος":arrow, "Κυβος":box, "Κωνος":cone, "Κυλινδρος":cylinder,
      "Ελλειψη":ellipsi, "Ελατηριο":helix, "Πυραμιδα":pyramid,
      "Δακτυλιος":ring, "Σφαιρα":sphere}

t=0

print """Καλως ορισατε στην παρουσιαση βασικων τρισδιαστατων σχηματων της
VPython, εαν θα θελατε εναν καταλογο των σχηματων που μπορειτε να
δημιουργησετε, γραψτε "Βοηθεια", αλλιως πληκτρολογηστε το ονομα του
σχηματος που θα θελατε να δημιουργησετε."""

while True:
    scene1=display(title='Demo',
     x=0, y=0, width=600, height=800,
     center=(0,0,0), background=(0,0,0))
    arxiko=raw_input("Παρακαλω δωστε την εντολη σας: ")
    if arxiko=="Βοηθεια":
        l=dict.keys()
        for i in l:
            print i
        continue
    elif arxiko in dict:
        while t<10:
            rate(1)
            obj=dict[arxiko]()
            t+=1
        scene1.delete()
        t=0
    else:
        print "Δεν δωσατε εγκυρη εντολη, παρακαλω ξαναπροσπαθηστε."


#Μακαριος Χρηστακης
#P.S.: Mr Sgarbas is the best
