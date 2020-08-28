import sqlite3
conn=sqlite3.connect("student.db")
cur=conn.cursor()


#Partie 2 :

#Partie 2-Question 1:
def insBU(nomE):
        res1=cur.execute("select count(nomE) from Etudiant where nomE=?",(nomE,))
        for row in res1:
            c=row[0]
        if(c==0):
            print("ce nom n'exist pas dans la base")
        else:
            res2=cur.execute("select dateInscripBU from Etudiant where nomE='%s'" % nomE)
            for row in res2:
                print(row[0])


#************************************************************

#Partie 2-Question 2:
def insCour(num_cours):
    rep=cur.execute(""" SELECT Etudiant.nomE ,Etudiant.prenomE FROM Etudiant,Inscrit,Cours 
                        where Etudiant.num_etu=Inscrit.num_etu AND Inscrit.num_cours=Cours.num_cours AND Cours.num_cours=?""",(num_cours,))
    print("nom    prenom")
    for row in rep:
        print(row[0]," ",row[1])

#************************************************************

#Partie 2-Question 3:
def RestEtu(num_etu):
    rep0=cur.execute("SELECT nomE,prenomE FROM ETUDIANT WHERE num_etu=?",(num_etu,))
    for row in rep0:
        print("-------------------------------------------------|")
        print( row[0],"        |    Moyennes      |               ")
        print(row[1], "       |---------------------------------|")
        print("              |  Elève |  Classe |  MAX  |  MIN  |")
        print("-------------------------------------------------|")
    rep1=cur.execute("select  AVG(note),MAX(note),MIN(note) from Resultat R,Cours C,Class where R.num_cours=C.num_cours GROUP BY nomC")
    c1=[] #Déclaration des tableaux
    c2=[] 
    c3=[]  
    for row in rep1:
        c1.append(row[0])#Mettre les resultats de 'rep1' dans les tableaux
        c2.append(row[1])
        c3.append(row[2])

    rep2=cur.execute("""SELECT nomC,note FROM Etudiant E,Inscrit I,Resultat R,Cours C,Class Cl 
                            where E.num_etu=R.num_etu AND R.num_cours=C.num_cours AND Cl.numClass=E.numClass 
                                AND E.num_etu=? GROUP BY nomE,nomC """,(num_etu,))
    i=0#Initialisation 
    for row in rep2:#Affichage des données 
        print(row[0],":      ","|",row[1],"|", c1[i],"|", c2[i],"|", c3[i],"|")
        print("-------------------------------------------------|")
        i=i+1  
    rep3=cur.execute("""select avg(note) from Etudiant E,Inscrit I,Resultat R,Cours C,Class Cl  
                   where E.num_etu=R.num_etu AND R.num_cours=C.num_cours AND Cl.numClass=E.numClass 
                                AND E.num_etu=? """,(num_etu,))
    
    for row in rep3:
        print("Moyenne génerale d'étudiant :" ,row[0])

#************************************************************

#Partie 2-Question 4:
def resultEchec():
    req=cur.execute("""SELECT nomE, prenomE, note, AVG(note), nomC FROM Etudiant E, Resultat R, Cours C 
                            WHERE E.num_etu=R.num_etu and R.num_cours=C.num_cours AND R.note<=10 GROUP BY nomC,numClass
                    """)
    for row in req:
        print(row[0],"    ",row[1],"  ",row[2],"  ",row[3],"  ",row[4])

#************************************************************

#Partie 2-Question 5:
def insr():
    res=cur.execute("""
     select nomE,prenomE from Etudiant E
                        where not exists (select * from Cours c
                                       where not exists ( select * from Inscrit I
                                                        where I.num_etu=E.num_etu and c.num_cours=I.num_cours
                                                        ))
                                                   """)
    print("nom    prenom")
    for row in res:
        print(row[0]," ",row[1])

#************************************************************

#Partie 2-Question 6:
def empLiv(Nlivre):
    rep=cur.execute("""SELECT nomE, prenomE, dateRoteur FROM Etudiant E, Pret p, Livre l 
                        where E.num_etu=p.num_etu and p.Nlivre=l.Nlivre AND l.Nlivre=? """,(Nlivre,))
    print("nom       prenom        date de retour")
    for row in rep:
       print(row[0],"   ",row[1],"   ",row[2])

#************************************************************

#Partie 2-Question 7:
def retard():
    res=cur.execute("select nomE,prenomE from Pret P,Etudiant E where E.num_etu=P.num_etu and P.dateRoteur>P.dateRoteurPrevue")
    print("nom et prenom:")
    for row in res:
        print(row[0],"  ",row[1],)

#************************************************************

#Partie 2-Question 8:
def noEmp():
    res=cur.execute("""SELECT nomE, prenomE, titre FROM Livre l, Pret p ,Etudiant E 
                        WHERE E.num_etu=p.num_etu AND p.Nlivre=l.Nlivre GROUP BY nomE""")
    print("nom      prenom      titre")
    for row in res:
     print(row[0],"  ",row[1],"  ",row[2])

#************************************************************

#Partie 2-Question 9:
def ResultTot():
    req=cur.execute("""SELECT nomclass,nomC, AVG(note) FROM Class Cl,Etudiant E,Resultat R,Cours C 
                        WHERE R.num_cours=C.num_cours AND R.num_etu=E.num_etu AND Cl.numClass=E.numClass group by nomclass,C.nomC """)
    for row in req:
        print(row[0],"   ",row[1],"   ",row[2])


#************************************************************

#Partie 2-Question 10:       
def changernom(n,newNom):
    import sqlite3
    conn=sqlite3.connect('student.db')
    cur=conn.cursor()
    res=cur.execute("update Cours set nomC=? where num_cours=?",(newNom,n))
    conn.commit()
    conn.close()
#*************************************************************
#    
#Partie 2-Question 11:     
def deleteC(n):
    import sqlite3
    conn=sqlite3.connect('student.db')
    cur=conn.cursor()
    cur.execute("delete from Cours where Cours.num_cours=?",(n,))
    conn.commit()
    conn.close()

#************************************************************

conn.commit()
conn.close()

