import MySQLdb


def CreateUser():
    db = MySQLdb.connect("127.0.0.1", "root", "password", "srmudb")
    mycursor = db.cursor()
    userName = raw_input("Enter the username:")
    userPass = raw_input("Enter the password:")
    userType = raw_input("Enter type of user:")
    fullname = raw_input("Enter Full Name:")
    phone    = raw_input("Enter phone number:")
    email    = raw_input("Enter email Id:")
    status   = raw_input("Enter status of user:")
    sql = "insert into employee(userName,userPass,userType,fullname,phone,email,status)values('%s','%s','%s','%s','%s','%s','%s')"
    values=(userName,userPass,userType,fullname,phone,email,status)
    mycursor.execute(sql % values)
    if mycursor.rowcount == 1:
        print("-" * 50, "\n\t\t\t\tUser Created Successfully\n", "-" * 50)
    else:
        print("-" * 50, "\n\t\t\t\tUser Creation Fail\n", "-" * 50)
    db.commit()
    db.close()


def AllUser():
    db = MySQLdb.connect("127.0.0.1", "root", "password", "srmudb")
    mycursor=db.cursor()
    sql="select * from employee"
    mycursor.execute(sql)
    print("\nUserName\t\tUser Type\t\tFull Name\t\t\t\tPhone\t\t\t\t\tEmail\t\t\t\t\t\t\t   Status")
    for row in mycursor:
        print(row[0], "\t\t\t",row[2], "\t\t\t", row[3], "\t\t\t", row[4], "\t\t\t", row[
            5], "\t\t\t\t", row[6])
    db.commit()
    db.close()

def AllProsp():
    db = MySQLdb.connect("127.0.0.1", "root", "password", "srmudb")
    mycursor=db.cursor()
    sql="select * from prospect"
    mycursor.execute(sql)
    print("ProspectID\t\tProspectName\t\tPhoneNo.\t\tAddress\t\t\t\t\t\tIntrested_In_Model\t\tColor\t\t  VisitDateTime\t\t   Hotness")
    for row in mycursor:
        print(row[0], "\t\t\t\t", row[1], "\t", row[2], "\t\t", row[3], "\t\t", row[4], "\t\t\t", row[
            5], "\t\t", row[6], "\t", row[7])
    db.commit()
    db.close()


def ChangePass():
    db = MySQLdb.connect("127.0.0.1", "root", "password", "srmudb")
    uName=raw_input("Which usename change the password:")
    mycursor = db.cursor()
    mycursor.execute("select * from employee")
    for row in mycursor:
        dbUser=row[0]
        if uName==dbUser:
            print("+-"*10,"%s type user"%row[2],"+-"*10)
            uPass=raw_input("Enter New Password:")
            mycursor = db.cursor()
            sql="update employee set userPass='%s' where userName='%s'"
            values=(uPass,uName)
            mycursor.execute(sql % values)
            break
    else:
        print("-" * 50, "\n\t\t\t\tUserName Not Found\n")
    if mycursor.rowcount == 1:
        print("-" * 50, "\n\t\t\t\tPassword Changed\n", "-" * 50)
    else:
        print("\n\t\t\t\tChanges Failed\n", "-" * 50)
    db.commit()
    db.close()


def Search():
    db = MySQLdb.connect("127.0.0.1", "root", "password", "srmudb")
    choose=input("Press 1 for search by Hotness and 2 for for search by Prospect Id:")
    mycursor=db.cursor()
    mycursor.execute("select * from prospect")
    try:
        if choose == 1:
            choose1 = raw_input("Enter your searching option:\nHot\nWarm\nCold")
            print("ProspectID\t\tProspectName\t\tPhoneNo.\t\tAddress\t\t\t\t\t\tIntrested_In_Model\t\tColor\t\t  VisitDateTime\t\t   Hotness")
            for row in mycursor:
                row1 = row[7]
                if choose1 == row1:
                    print(row[0], "\t\t\t\t", row[1], "\t", row[2], "\t\t", row[3], "\t\t", row[4], "\t\t\t", row[
                        5], "\t\t", row[6], "\t", row[7])
                    break
            else:
                print("-" * 50, "\n\t\t\t\tRecord Not Found\n", "-" * 50)
        elif choose == 2:
            try:
                prospid = input("Enter prospect ID:")
                print("ProspectID\t\tProspectName\t\tPhoneNo.\t\tAddress\t\t\t\t\t\tIntrested_In_Model\t\tColor\t\t  VisitDateTime\t\t   Hotness")
                for row in mycursor:
                    row1 = row[0]
                    if prospid == row1:
                        print(row[0], "\t\t\t\t", row[1], "\t", row[2], "\t\t", row[3], "\t\t", row[4], "\t\t\t", row[
                            5], "\t\t", row[6], "\t", row[7])
                        break
                else:
                    print("-" * 50, "\n\t\t\t\tRecord Not Found\n", "-" * 50)
            except (NameError, SyntaxError):
                print("-" * 50, "\n\t\t\t\tInvalid Prospect Id Try Again\n")
        else:
            print("\n\t\t\t\tWrong Option\n", "-" * 50)

    except SyntaxError:
        print("-" * 50, "\n\t\t\t\tInvalid Entry Try Again\n", "-" * 50)
    db.commit()
    db.close()



def ActiveOrDeactive():
    db = MySQLdb.connect("127.0.0.1", "root", "password", "srmudb")
    uName=raw_input("Which usename change the Activation Status:")
    mycursor = db.cursor()
    mycursor.execute("select * from employee")
    for row in mycursor:
        dbUser=row[0]
        if uName==dbUser:
            print("\n","-<>-"*10,"%s type user"%row[2],"-<>-"*10)
            uStatus=raw_input("Enter Status activated or deactivated")
            mycursor = db.cursor()
            if uStatus == "activated":
                sql = "update employee set status ='%s' where userName='%s'"
                values = (uStatus, uName)
                mycursor.execute(sql % values)
                break
            elif uStatus == "deactivated":
                sql = "update employee set status ='%s' where userName='%s'"
                values = (uStatus, uName)
                mycursor.execute(sql % values)
                break
            else:
                print("-" * 70,"\n\t\tChoose Only activated Or deactivated(case sensitive)\n")
                break

    else:
        print("-" * 70,"\n\t\t\t\tUserName Not Found\n")
    if mycursor.rowcount == 1:
        print("-" * 50, "\n\t\t\t\tStatus Changed\n", "-" * 50)
    else:
        print("\n\t\t\t\t\t\tChanges Failed\n", "-" * 70)
    db.commit()
    db.close()

def ManageModel():
    choose=input("Choose Your Modal Option:\n1: Add\n2: View\n3: Update")
    db = MySQLdb.connect("127.0.0.1", "root", "password", "srmudb")
    mycursor = db.cursor()
    if choose==1:
        modalId   = raw_input("\nEnter Modal Id:")
        modalName = raw_input("\nEnter Modal Name:")
        Price     = input("\nEnter Price:")
        sql = "insert into modal(modalId,modalName,Price)values('%s','%s',%f)"
        values=(modalId,modalName,Price)
        mycursor.execute(sql % values)
        if mycursor.rowcount == 1:
            print("-" * 50, "\n\t\t\t\tModal Added Successfully\n", "-" * 50)
        else:
            print("-" * 50, "\n\t\t\t\tModal Adding Failed\n", "-" * 50)
        db.commit()
        db.close()
    elif choose==2:
        mycursor.execute("select * from modal")
        print("\nModal Id\t\t\t\tModal Name\t\t\t\t\t\t\tPrice\n")
        for row in mycursor:
            print(row[0],"\t\t",row[1],"\t\t\t\t\t",row[2])
        db.commit()
        db.close()
    elif choose==3:
        option=raw_input("Choose your option for update:\npress a: Modal Id\npress b: Modal Name\npress c: Price")
        if option=='a':
            modal=raw_input("Enter Modal Name(case sensitive):")
            mycursor.execute("select * from modal")
            for row in mycursor:
                if modal==row[1]:
                    update=raw_input("Enter New Modal Id:")
                    mycursor=db.cursor()
                    sql="update modal set modalId='%s' where modalName='%s'"
                    values=(update,modal)
                    mycursor.execute(sql % values)
                    db.commit()
                    break
            else:
                print("-" * 50, "\n\t\t\t\tModal Name Not Found\n", "-" * 50)
            if mycursor.rowcount == 1:
                print("-" * 50, "\n\t\t\t\tModal Id Changed Successfully\n", "-" * 50)
            else:
                print("-" * 50, "\n\t\t\t\tChanges Failed\n", "-" * 50)
            db.close()
        elif option=='b':
            modal=raw_input("Enter Modal Id(case sensitive):")
            mycursor.execute("select * from modal")
            for row in mycursor:
                if modal == row[0]:
                    update = raw_input("Enter New Modal Name:")
                    mycursor = db.cursor()
                    sql = "update modal set modalName='%s' where modalId='%s'"
                    values = (update, modal)
                    mycursor.execute(sql % values)
                    break
            else:
                print("-" * 50, "\n\t\t\t\tModal ID Not Found\n", "-" * 50)
            if mycursor.rowcount == 1:
                print("-" * 50, "\n\t\t\t\tModal Name Changed Successfully\n", "-" * 50)
            else:
                print("-" * 50, "\n\t\t\t\tChanges Failed\n", "-" * 50)
            db.commit()
            db.close()
        elif option=='c':
            modal = raw_input("Enter Modal Id(case sensitive):")
            mycursor.execute("select * from modal")
            for row in mycursor:
                if modal == row[0]:
                    update = input("Enter New Modal Price:")
                    mycursor = db.cursor()
                    sql = "update modal set Price=%d where modalId='%s'"
                    values = (update, modal)
                    mycursor.execute(sql % values)
                    break
            else:
                print("-" * 50, "\n\t\t\t\tModal Name Not Found\n", "-" * 50)
            if mycursor.rowcount == 1:
                print("-" * 50, "\n\t\t\t\tModal Price Changed Successfully\n", "-" * 50)
            else:
                print("-" * 50, "\n\t\t\t\tChanges Failed\n", "-" * 50)
            db.commit()
            db.close()
        else:
            print("-" * 50, "\n\t\t\t\tWrong Choice\n", "-" * 50)
    else:
        print("Wrong option")


def final():
    print("-" * 50, "\n\t\t\t\tLogin Successfully\n\n\t\t\t\tWelcome Administrator\n", "-" * 50)
    while True:
        try:
            choice1 = input(
                "\n\t\t\t\tWelcome into Admin Module\n1: Create User\n2: View All User\n3: View All Prospect\n"
                "4: Change Password\n5: Search Prospect\n6: Activate Or Deactivate Account\n7: Manage All Model\n"
                "8: SignOut\nEnter your Choice:")
            if choice1 == 1:
                CreateUser()
            elif choice1 == 2:
                AllUser()
            elif choice1 == 3:
                AllProsp()
            elif choice1 == 4:
                ChangePass()
            elif choice1 == 5:
                Search()
            elif choice1 == 6:
                ActiveOrDeactive()
            elif choice1 == 7:
                ManageModel()
            elif choice1 == 8:
                print("-" * 50, "\n\t\t\t\tThank You For Visiting\n", "-" * 50)
                exit(0)
            else:
                print("Wrong Option")
        except SyntaxError:
            print("-" * 50, "\n\t\t\t\tInvalid Entry Try Again\n", "-" * 50)



