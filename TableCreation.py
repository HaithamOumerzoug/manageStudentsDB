import sqlite3
conn=sqlite3.connect('student.db')
cur=conn.cursor()
#Création des tables :

cur.executescript("""

create table Auteur(
    Nauteur integer,
    nomA varchar(20),
    nomB varchar(20),
    nationalite varchar(10),
    constraint c1 primary key(Nauteur)
);

create table Livre(
    Nlivre integer,
    num_ISBN integer,
    titre varchar(20),
    nbPages integer,
    annéesS integer,
    prix integer,
    constraint c2 primary key(Nlivre)
);

create table Possede(
    Nlivre integer,
    Nauteur integer,
    constraint c3 foreign key (Nlivre) references Livre(Nlivre),
    constraint c4 foreign key (Nauteur) references Auteur(Nauteur)
);

create table Pret (
    Npret integer,
    num_etu integer,
    Nlivre integer,
    datePret date,
    dateRoteur date,
    dateRoteurPrevue date,
    constraint c5 primary key (Npret),
    constraint c6 foreign key (num_etu) references Etudiant(num_etu),
    constraint c7 foreign key (Nlivre) references Livre(Nlivre)
);

create table Etudiant(
    num_etu integer,
    nomE varchar(20),
    prenomE varchar(20),
    datenaissance date,
    ville varchar(20),
    dateInscripBU date,
    dateAbs date,
    numClass integer,
    constraint c8 primary key (num_etu),
    constraint c9 foreign key (numClass) references  Class(numClass)
);

create table Class(
    numClass integer,
    nomclass varchar(20),
    constraint c10 primary key (numClass)
);

create table Cours(
    num_cours integer,
    nomC varchar(20),
    nb_heures integer,
    num_ens integer,
    constraint c11 primary key(num_cours),
    constraint c12 foreign key(num_ens) references Cours(num_ens)
);

create table Enseignant(
    num_ens integer,
    nomP varchar(20),
    prenomP varchar(20),
    specialite varchar(20),
    departement varchar(20),
    constraint c13 primary key (num_ens)
);

create table Resultat(
    num_etu integer,
    num_cours integer,
    note float,
    constraint c14 foreign key (num_etu) references Etudiant(num_etu),
    constraint c15 foreign key (num_cours) references Cours(num_cours)
);

create table Charge(
    num_ens integer,
    num_cours integer,
    nbH float,
    constraint c16 foreign key (num_ens) references Enseignant(num_ens),
    constraint c17 foreign key (num_cours) references Cours(num_cours)
);

create table Inscrit(
    num_etu integer,
    num_cours integer,
    dateInsC date,
    constraint c18 foreign key(num_etu) references Etudiant(num_etu),
    constraint c19 foreign key(num_cours) references Cours(num_cours)
);

""")

conn.commit()
conn.close()
