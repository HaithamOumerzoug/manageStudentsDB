import sqlite3
import matplotlib.pyplot as plt
conn=sqlite3.connect('student.db')
cur=conn.cursor()
res=cur.execute("""select  count(nt) from (select num_etu,avg(note) as 'nt'
                                                     from Resultat group by num_etu) where nt between 12 and 14""")
for row in res:
    a=row[0]
res=cur.execute("""select  count(nt) from (select num_etu,avg(note) as 'nt'
                                                     from Resultat group by num_etu) where nt between 8 and 12""")
for row in res:
    b=row[0]
res=cur.execute("""select  count(nt) from (select num_etu,avg(note) as 'nt'
                                                     from Resultat group by num_etu) where nt<=8""")
for row in res:
    c=row[0]
res=cur.execute("""select  count(nt) from (select num_etu,avg(note) as 'nt'
                                                     from Resultat group by num_etu) where nt>14""")
for row in res:
    d=row[0]
slices=[a,b,c,d]
print(slices)
note=['12<note<14','8<note<12','note<=8','note>14']
cols=['c','g','r','y']
plt.pie(
    slices,
   labels=note,
   colors=cols,
   startangle=90,
   shadow=True,
   explode=(0,0.1,0,0),
   autopct="%1.2f%%"
   )
plt.title("camembert des notes")
plt.show()



