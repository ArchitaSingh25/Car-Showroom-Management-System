import MySQLdb
import Admin
import Monitor

def Login():
    uName=raw_input("Enter user name:")
    uPass=raw_input("Enter password:")
    db = MySQLdb.connect("127.0.0.1", "root", "password", "srmudb")
    mycursor=db.cursor()
    mycursor.execute("select * from employee")
    for row in mycursor:
        dbUser=row[0]
        dbPass=row[1]
        dbStatus=row[6]
        if uName==dbUser:
            if uPass==dbPass:
                dbtype=row[2]
                if dbStatus=="activated":
                    if dbtype == "admin":
                        Admin.final()
                        break
                    else:
                        Monitor.final(uName)
                        break

    else:
        print("Login Authentication Failed")
    db.commit()
    db.close()

Login()