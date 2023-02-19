 
a=0
b=0
c=0
cho=0

#create module----------------

def create1():
    import sqlite3
    conn = sqlite3.connect("test.db")
     
    cur = conn.cursor()
    cur.execute("create table labours (sno int,occupation varchar(20),wages int)")
    conn.commit()
        
    print("created1")
     
    
def create2(): 
    import sqlite3
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("create table rawmaterials_equipment (sno int,rawmat_equip varchar(20),price_rent int)")
    conn.commit()
    
    print("created2")
    
    
def create3():
    import sqlite3
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("create table miscellaneous(sno int,expenses varchar(20),cost int)")
    conn.commit()
    
    print("created3")


def create4():
    import sqlite3
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("create table subcontractor(sno int,occupation varchar(20),salary int)")
    conn.commit()
    
    print("created4")

#add module----------------------

 
    
def add1():
     
    import sqlite3
    conn  =  sqlite3 . connect ( 'test.db' )
    cur  =  conn.cursor ()
    s_no = input('sno:')
    s_occ = input('occupation:')
    s_wages = input('wages:')
    cur.execute("""
    INSERT INTO labours(sno, occupation, wages)
    VALUES (?,?,?)
    """, (s_no, s_occ, s_wages))
    conn.commit()
    print("----------------------------------------------------")
         

    
    menu()

 

def add2():
    
    import sqlite3
    conn  =  sqlite3 . connect ( 'test.db' )
    cur  =  conn.cursor ()
    s_no = input('sno:')
    s_mat = input('rawmat_equip:')
    s_price = input('price_rent:')
    cur.execute("""
    INSERT INTO rawmaterials_equipment(sno, rawmat_equip, price_rent)
    VALUES (?,?,?)
    """, (s_no, s_mat, s_price))
    conn.commit()
    print("----------------------------------------------------")
         

    
    menu()

 
    
def add3():     
     
    import sqlite3
    conn  =  sqlite3 . connect ( 'test.db' )
    cur  =  conn.cursor ()
    s_no = input('sno:')
    s_exp = input('expenses:')
    s_cost = input('cost:')
    cur.execute("""
    INSERT INTO miscellaneous(sno, expenses, cost)
    VALUES (?,?,?)
    """, (s_no, s_exp, s_cost))
    conn.commit ()
    print("----------------------------------------------------")
         

    
    menu()

 
def add4():    
    
    import sqlite3
    conn  =  sqlite3 . connect ( 'test.db' )
    cur  =  conn.cursor ()
    s_no = input('sno:')
    s_occ = input('occupation:')
    s_sal = input('salary:')
    cur.execute("""
    INSERT INTO subcontractor(sno, occupation, salary)
    VALUES (?,?,?)
    """, (s_no, s_occ, s_sal))
    conn.commit ()
    print("----------------------------------------------------")
         

    
    menu()

 
    

    
#update module--------------

def update1():
    
    import sqlite3
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    s_no = input('sno:') 
    s_wages = input('wages:')
    
    cur.execute("update labours set wages='" + s_wages + "' where sno="+s_no)
    conn.commit()
     
    print("updated!")
    print("----------------------------------------------------")
         

    
    menu()

def update2():
    
    import sqlite3
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    s_no = input('sno:')
    s_price = input('price_rent:')
    
    cur.execute("update rawmaterials_equipment set price_rent='" + s_price +"' where sno="+s_no)
    conn.commit()
     
    print("updated!")
    print("----------------------------------------------------")
         

    
    menu()

def update3():
    
    import sqlite3
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    s_no = input('sno:')
    s_cost = input('cost:')
    cur.execute("update miscellaneous set cost='" + s_cost +"' where sno="+s_no)
    conn.commit()
     
    print("updated!")
    print("----------------------------------------------------")
         

    
    menu()

def update4():
    
    import sqlite3
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    s_no = input('sno:')
    s_sal = input('salary:')
    cur.execute("update subcontractor set salary='" + s_sal +"' where sno="+s_no)
    conn.commit()
     
    print("updated!")
    print("----------------------------------------------------")
         

    
    menu()

#delete module------------

def delete1():
    
    import sqlite3
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    s_no = input('sno:')
    cur.execute("delete from labours where sno = "+s_no)
    conn.commit()
    conn.close()
    print("deleted")
    print("----------------------------------------------------")
         

    
    menu()

def delete2():
     
    import sqlite3
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    s_no = input('sno:')
    cur.execute("delete from rawmaterials_equipment where sno = "+s_no)
    conn.commit()
    conn.close()
    print("deleted")
    print("----------------------------------------------------")
         

    
    menu()

def delete3():
     
    import sqlite3
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    s_no = input('sno:')
    cur.execute("delete from miscellaneous where sno = "+s_no)
    conn.commit()
    conn.close()
    print("deleted")
    print("----------------------------------------------------")
         

    
    menu()

def delete4():
     
    import sqlite3
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    s_no = input('sno:')
    cur.execute("delete from subcontractor where sno = "+s_no)
    conn.commit()
    conn.close()
    print("deleted")
    print("----------------------------------------------------")
         

    
    menu()

#view module---------------

def view1():
     
    import sqlite3
    con = sqlite3.connect('test.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM labours')
    rows = cur.fetchall()
    for row in rows:

        print(row)
    print("--------------------------------------------------")
         
         
    
    menu()

    

def view2():
     
    import sqlite3
    con = sqlite3.connect('test.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM rawmaterials_equipment')
    rows = cur.fetchall()
    for row in rows:

        print(row)
    print("---------------------------------------------------")

          
    menu()

def view3():
     
    import sqlite3
    con = sqlite3.connect('test.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM miscellaneous')
    rows = cur.fetchall()
    for row in rows:

        print(row)
    print("----------------------------------------------------")
         

    menu()

def view4():
     
    import sqlite3
    con = sqlite3.connect('test.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM subcontractor')
    rows = cur.fetchall()
    for row in rows:

        print(row)
    print("----------------------------------------------------")
         

    menu()

#sum module----------------
    
def view5():
 import sqlite3
 con = sqlite3.connect('test.db')
 y=int(input("enter the proposed amount:"))
 cur = con.cursor()
 cur.execute('SELECT sum(wages) FROM labours')
 rows = cur.fetchall()
 n1=0
 for row in rows:

    print(int(row[0]))
    n1=int(row[0])

 cur = con.cursor()
 cur.execute('SELECT sum(price_rent) FROM rawmaterials_equipment')
 rows = cur.fetchall()
 n2=0
 for row in rows:

    print(int(row[0]))
    n2=int(row[0])

 cur = con.cursor()
 cur.execute('SELECT sum(cost) FROM miscellaneous')
 rows = cur.fetchall()
 n3=0
 for row in rows:

    print(int(row[0]))
    n3=int(row[0])

 cur = con.cursor()
 cur.execute('SELECT sum(salary) FROM subcontractor')
 rows = cur.fetchall()
 n4=0
 for row in rows:

    print(int(row[0]))
    n4=int(row[0])
    #print (n)
 x=(n1+n2+n3+n4)
 print("----------")
 print(x)
 print(y)
 print("----------")
 print(y-x)
 print("net result")
 print("----------------------------------------------------")

 menu()




    



def menu():
    print("MASONRY WORK MANAGEMENT SYSTEM")
    print("Press ")
    print("LABOUR")
    print("1 to Add labour")
    print("2 to update labour ")
    print("3 to delete labour")
    print("4 to view labour")
    print("-----------------")
    print("RAWMATERIALS AND EQUIPMENT")
    print("5 to Add rawmat")
    print("6 to update rawmat ")
    print("7 to delete rawmat")
    print("8 to view rawmat")
    print("-----------------")
    print("MISCELLANEOUS EXPENDITURE")
    print("9 to add miscellaneous")
    print("10 to update micellaneous")
    print("11 to delete miscellaneous")
    print("12 to view miscellaneous")
    print("-----------------")
    print("SUBCONTRACTOR")
    print("13 to add subcontractor")
    print("14 to update subcontractor")
    print("15 to delete subcontractor")
    print("16 to view subcontractor")
    print("-----------------")
    print("17 to show the total value of investment")
    
    print("18 exit")

    print("---------------------------------------------------")
        
         
     

    cho=int(input("enter your choice: "))
    if (cho==1):
        add1()
        

    elif (cho==2):
         update1()

    elif (cho==3):
        delete1()

    elif (cho==4):
        view1()
        
    elif (cho==5):
        add2()
        

    elif (cho==6):
         update2()

    elif (cho==7):
        delete2()

    elif (cho==8):
        view2()

    elif (cho==9):
        add3()
        

    elif (cho==10):
         update3()

    elif (cho==11):
        delete3()

    elif (cho==12):
        view3()

    elif (cho==13):
        add4()
        

    elif (cho==14):
         update4()

    elif (cho==15):
        delete4()

    elif (cho==16):
        view4()


    elif (cho==17):
        view5()

    elif(cho==18):
        exit(0)
        
    else:
        print("Invalid Choice")
        menu()

menu()  
    

