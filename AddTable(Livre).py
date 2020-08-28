import sqlite3
conn=sqlite3.connect('student.db')
cur=conn.cursor()
cur.execute("delete from Livre")
cur.execute("""
insert into Livre values(1,1200,'le maroc',100,2011,100,1),
                         (2,1202,'technologie',100,2012,150,2),
                         (3,1000,'science',120,2010,200,3),
                         (4,1222,'sahara',200,2009,100,4)
""")
conn.commit()
conn.close()
