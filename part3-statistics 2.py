import sqlite3
import matplotlib.pyplot as plt
conn=sqlite3.connect('student.db')
cur=conn.cursor()
res=cur.execute("""select  nt,count(nt) from (select num_etu,avg(note) as 'nt'
                                                       from Resultat group by num_etu) group by nt""")
x=[]
y=[]
x1=list(cur)
for i in range(0,len(x1)):
    x.append(x1[i][0])
    y.append(x1[i][1])
plt.bar(x,y,0.05)
plt.xlabel("les notes")
plt.ylabel("le nombre d'eleve")
plt.title("histogrammes des notes")
plt.show()



