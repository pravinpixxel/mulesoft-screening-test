import sqlite3
con=sqlite3.connect('user.db')
#con.execute("create table users(NAME,ACTOR,ACTRESS,DIRECTOR,YEAR);")
def insertData(name,actor,actress,director,year):
    qry=f'insert into users (NAME,ACTOR,ACTRESS,DIRECTOR,YEAR) values ("{name}","{actor}","{actress}","{director}","{year}");'
    con.execute(qry)
    con.commit()
    print("add")

def select(actor):
    qry='select * from users where actor="'+actor+'";'
    result=con.execute(qry)
    for row in result:
        print(row)

ch="y"
while(ch.lower()!='n'):
    c=int(input())
    if(c==1):
        print("add record")
        name=input("Enter the name of the movie:")
        actor=input("Enter the name of the actor:")
        actress=input()
        director=input()
        year=input()
        insertData(name,actor,actress,director,year)
    elif (c==2):
        print("select")
        select(input("ACTOR NAME:"))
    else:
        print("Invalied option:" + c)
    ch = input("Do you want to continue[Y/n]: ")