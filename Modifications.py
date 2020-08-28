import sqlite3
conn=sqlite3.connect('student.db')
cur=conn.cursor()

#Partie 1-B-Modification :

#Question 1,2 et 3
cur.execute("""
PRAGMA foreign_keys=off;
BEGIN TRANSACTION;
create table Etudiant1(
   num_etu integer,
   nomE varchar(30),
   prenomE varchar(20),
   datenaissance date,
   ville varchar(20),
   dateInscripBU date,
   dateAbs date,
   numClass integer,
   constraint c08 primary key (num_etu),
   constraint c09 foreign key (numClass) references  Class(numClass)
  );

#cur.execute("insert into Etudiant1 select * from Etudiant")
#cur.execute("drop table Etudiant")
#cur.execute("alter table Etudiant1 rename to Etudiant")
#cur.execute("alter table Etudiant  add email varchar(20)")
#cur.execute("alter table Etudiant add adresse varchar(20)")
COMMIT;
PRAGMA foreign_keys=on;
""")

#Qustion 4 :
cur.executescript(""" 
PRAGMA foreign_keys=off;
Alter table Pret RENAME TO oldpret;
Create table Pret (
    Npret integer, 
    num_etu integer, 
    Nlivre integer, 
    datePret date, 
    dateRetour date, 
    DateRetourPrevue date
);
INSERT INTO Pret SELECT * FROM oldpret;
Drop table oldpret;
PRAGMA foreign_keys=on;
""")

#Question 5 :
cur.executescript("""
PRAGMA foreign_keys=off;

BEGIN TRANSACTION;

ALTER TABLE Pret RENAME TO old_Pret;

CREATE TABLE Pret
(
    Npret integer, 
    num_etu integer, 
    Nlivre integer, 
    datePret date, 
    dateRetour date, 
    DateRetourPrevue date,
Constraint c05 PRIMARY KEY(Npret),
Constraint c06 FOREIGN KEY(num_etu) REFERENCES Etudiant(num_etu),
Constraint c07 FOREIGN KEY(Nlivre) REFERENCES Livre(Nlivre)
);

INSERT INTO Pret SELECT * FROM old_Pret;

COMMIT;

PRAGMA foreign_keys=on;

Drop table old_Pret
""")
#Question 6:
cur.executescript(""" 

PRAGMA foreign_keys=off;
BEGIN TRANSACTION;
ALTER TABLE Livre RENAME TO old_Livre;
Create table Livre(
    Nlivre integer, 
    num_ISBN integer, 
    titre varchar(10), 
    nbPages integer, 
    annéeS date, 
    prix integer,
    Nauteur integer,
    Constraint C02 PRIMARY KEY(Nlivre),
    Constraint c001 FOREIGN KEY(Nauteur) REFERENCES Auteur(Nauteur)
);

INSERT INTO Livre Select * FROM old_Livre;
COMMIT;
PRAGMA foreign_keys=on;
Drop tble old_Livre;
""")
#Question 7:
cur.executescript(""" 

PRAGMA foreign_keys=off;

Drop table Possede;
 
PRAGMA foreign_keys=on;

""")

#Question 8:
cur.executescript(""" 

PRAGMA foreign_keys=off;
BEGIN TRANSACTION;
Create table New_Livre(
    Nlivre integer, 
    Nauteur integer,
    num_ISBN integer, 
    titre varchar(20), 
    nbPages integer, 
    annéeS date, 
    prix integer,
    Constraint c02 PRIMARY KEY(Nlivre),
    Constraint c001 FOREIGN KEY(Nauteur) REFERENCES Auteur(Nauteur),
    Constraint c0001 UNIQUE(titre)
);
insert INTO New_Livre select * from Livre;
Drop table Livre;
ALTER TABLE New_Livre RENAME TO Livre;
COMMIT;

PRAGMA foreign_keys=on;

""")
#9:
cur.executescript("""
ALTER TABLE Livre ADD langue varchar(20) ;
ALTER TABLE Livre ADD NbreExemplaire integer;
 """)

#Question 10
cur.executescript("""
PRAGMA foreign_keys=off;
BEGIN TRANSACTION;
Create table New_Livre(
    Nlivre integer, 
    Nauteur integer,
    num_ISBN integer, 
    titre varchar(20), 
    nbPages integer, 
    annéesS date, 
    prix integer,
    langue varchar(20),
    NbreExemplaires integer,
    Constraint c012 PRIMARY KEY(Nlivre),
    Constraint c0011 FOREIGN KEY(Nauteur) REFERENCES Auteur(Nauteur),
    Constraint c0001l UNIQUE(titre),
    Constraint c0012 UNIQUE(num_ISBN)

);
insert INTO New_Livre select * from Livre;
Drop table Livre;
ALTER TABLE New_Livre RENAME TO Livre;
COMMIT;

PRAGMA foreign_keys=on;
 """)
#Question 11:
cur.executescript("""
PRAGMA foreign_keys=off;

BEGIN TRANSACTION;
CREATE TABLE Pret2
(
    Npret integer, 
    num_etu integer, 
    Nlivre integer, 
    datePret date, 
    dateRetour date, 
    DateRetourPrevue date,
Constraint c0235 PRIMARY KEY(Npret),
Constraint c0236 FOREIGN KEY(num_etu) REFERENCES Etudiant(num_etu),
Constraint c0237 FOREIGN KEY(Nlivre) REFERENCES Livre(Nlivre),
Constraint cSA check(dateRetour>=datePret)
);

INSERT INTO Pret2 SELECT * FROM Pret;
Drop table Pret;
ALTER TABLE Pret2 RENAME TO Pret;
COMMIT;

PRAGMA foreign_keys=on;


""")
conn.commit()
conn.close()
