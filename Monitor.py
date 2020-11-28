import MySQLdb
import Admin


def add_new_prospect():
    db = MySQLdb.connect("127.0.0.1", "root", "password", "srmudb")
    mycursor = db.cursor()
    prospName = raw_input("Enter the Full name:")
    prospPhone = raw_input("Enter the phone no.:")
    prospAddress = raw_input("Enter Address of user:")
    interestModel = raw_input("Enter model ID interested in:")
    interestColour = raw_input("Enter interested colour:")
    dateTime=input("Enter Date Time YYYYMMDDHHMMSS=")
    hotness= raw_input("Enter hotness of prospect")
    mycursor.execute("select * from modal")
    for row in mycursor:
        if interestModel==row[0]:
            mycursor = db.cursor()
            sql = "insert into prospect(prospName,prospPhone,prospAddress,interestedModel," \
                  "interestedColour,date_of_visit,hotness)values('%s','%s','%s','%s','%s',%d,'%s')"
            values = (prospName, prospPhone, prospAddress, interestModel, interestColour, dateTime, hotness)
            mycursor.execute(sql % values)

    if mycursor.rowcount == 1:
        print("-" * 50, "\n\t\t\t\tUser Added Successfully\n", "-" * 50)
    else:
        print("-" * 50, "\n\t\t\t\tUser Adding Failed Try Again\n", "-" * 50)
    db.commit()
    db.close()


def update_prospect_detail():
    choice=raw_input("\npress 1: To update phone number\npress 2: To update interest model\npress 3:" \
          " To update colour\npress 4: To update hotness\nEnter your choice:")
    if choice=='1':
        db = MySQLdb.connect("127.0.0.1", "root", "password", "srmudb")
        mycursor = db.cursor()
        sql="update prospect set prospPhone='%s' where prospName='%s'"
        prospPhone=raw_input("Enter new phone no.")
        prospName=raw_input("Enter name of prospect whose no. is to be changed")
        values=(prospPhone,prospName)
        mycursor.execute(sql % values)
        if mycursor.rowcount == 1:
            print("-" * 50, "\n\t\t\t\tDetail Update Successfully\n", "-" * 50)
        else:
            print("-" * 50, "\n\t\t\t\tUpdation Failed Try Again\n", "-" * 50)
        db.commit()
        db.close()
    elif choice=='2':
        db = MySQLdb.connect("127.0.0.1", "root", "password", "srmudb")
        mycursor = db.cursor()
        sql = "update prospect set interestedModel='%s' where prospName='%s'"
        interestModel= raw_input("Enter new model no.")
        prospName = raw_input("Enter name of prospect whose no. is to be changed")
        values = (interestModel, prospName)
        mycursor.execute(sql % values)
        if mycursor.rowcount == 1:
            print("-" * 50, "\n\t\t\t\tDetail Update Successfully\n", "-" * 50)
        else:
            print("-" * 50, "\n\t\t\t\tUpdation Failed Try Again\n", "-" * 50)
        db.commit()
        db.close()
    elif choice =='3':
        db = MySQLdb.connect("127.0.0.1", "root", "password", "srmudb")
        mycursor = db.cursor()
        sql = "update prospect set interestedColour='%s' where prospName='%s'"
        interestColour = raw_input("Enter colour")
        prospName = raw_input("Enter name of prospect whose no. is to be changed")
        values = (interestColour, prospName)
        mycursor.execute(sql % values)
        if mycursor.rowcount == 1:
            print("-" * 50, "\n\t\t\t\tDetail Update Successfully\n", "-" * 50)
        else:
            print("-" * 50, "\n\t\t\t\tUpdation Failed Try Again\n", "-" * 50)
        db.commit()
        db.close()
    elif choice =='4':
        db = MySQLdb.connect("127.0.0.1", "root", "password", "srmudb")
        mycursor = db.cursor()
        sql = "update prospect set hotness='%s' where prospName='%s'"
        hotness = raw_input("Enter hotness")
        prospName = raw_input("Enter name of prospect whose no. is to be changed")
        values = (hotness, prospName)
        mycursor.execute(sql % values)
        if mycursor.rowcount == 1:
            print("-" * 50, "\n\t\t\t\tDetail Update Successfully\n", "-" * 50)
        else:
            print("-" * 50, "\n\t\t\t\tUpdation Failed Try Again\n", "-" * 50)
        db.commit()
        db.close()
    else:
        print("-" * 50, "\n\t\t\t\tWrong Choice\n", "-" * 50)

def ChangePass(LoginName):
    db = MySQLdb.connect("127.0.0.1", "root", "password", "srmudb")
    uName = raw_input("Which usename change the password:")
    mycursor = db.cursor()
    mycursor.execute("select * from employee")
    for row in mycursor:
        dbUser = row[0]
        if uName == dbUser:
            if LoginName == uName:
                uPass = raw_input("Enter New Password:")
                mycursor = db.cursor()
                sql = "update employee set userPass='%s' where userName='%s'"
                values = (uPass, uName)
                mycursor.execute(sql % values)
                break
            else:
                print("-" * 50, "\n\t\t\t\tEnter Your UserName\n")
                break
    else:
        print("-" * 50, "\n\t\t\t\tUserName Not Found\n")
    if mycursor.rowcount == 1:
        print("-" * 50, "\n\t\t\t\tPassword Changed\n", "-" * 50)
    else:
        print("\n\t\t\t\tChanges Failed\n", "-" * 50)
    db.commit()
    db.close()



def final(LoginName):
    print("-" * 50, "\n\t\t\t\tLogin Successfully\n\n\t\t\tWelcome Prospect Monitor\n", "-" * 50)
    while True:
        choice1 = raw_input("\n\t\t\t\tWelcome into Monitor Module\n1: Add New Prospect\n2: View All Propect\n3: Update Propect Detail\n"
            "4: Search Prospect\n5: Change Password\n6: Signout\nEnter your Choice:")
        if choice1 == '1':
            add_new_prospect()
        elif choice1 =='2':
            Admin.AllProsp()
        elif choice1 == '3':
            update_prospect_detail()
        elif choice1 == '4':
            Admin.Search()
        elif choice1 == '5':
            ChangePass(LoginName)
        elif choice1 == '6':
            print("-" * 50, "\n\t\t\t\tThank You For Visiting\n", "-" * 50)
            exit(0)
        else:
            print("-" * 50, "\n\t\t\t\tWrong Option\n", "-" * 50)