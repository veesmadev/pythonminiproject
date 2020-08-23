import pickle
import os.path
from os import path

def newuser():
    print("\n")
    print("Enter username")
    username=input()
    print("Enter pasword")
    password=input()
    users_file = open ( "users.pkl" , "rb")
    users_dict = pickle.load(users_file)
    users_file.close()
    users_dict.update( {username : password } )
    users_file = open ( "users.pkl" , "wb")
    pickle.dump(users_dict, users_file)
    users_file.close()
    null_acc = { 0 : "None" }
    user = open ( (username + ".pkl" ) , "wb" )
    pickle.dump( null_acc , user)
    user.close()
    print("User ", username, "created successfully !!!")
    

def showresult(username) :
    print("\n")
    print("Your test results are shown below \n\n")
    ####
    user = open ( (username + ".pkl" ) , "rb" )
    usertest = pickle.load(user)  ###User test details
    user.close()
    score = 0
    totalscore = 0
    for key, value in usertest.items() :
        print(key, ".  ", value[0])

        count = 0
        for option in value[1] :
            count +=1
            print ( "(" , count ,")",option)

        print("Correct Answer is option ", value[2])
        print("Your answer is option ",value[3])

        if value[2] == value[3] :
            score +=1
        totalscore +=1
        print("\n")

    print("Your score is ", score ,"/", totalscore, "\n")
    
    

def user():
    print("\n")
    while True:
        print("Enter 0 to go back. \n To continue press any key and enter.")
        back = input()
        if back == "0" :
            return
        print("Enter username")
        username=input()
        print("Enter password")
        password=input()
        users_file = open ( "users.pkl" , "rb")
        users_dict = pickle.load(users_file)
        users_file.close()
        if username in users_dict.keys():
            if users_dict[username] == password :
                print("Welcome ", username )
                ## Continue user test sequence
                user = open ( (username + ".pkl" ) , "rb" )
                usertest = pickle.load(user)  ###User test details
                user.close()
                if 0 in usertest.keys()  :
                    print("You have not appeared any test !!!")
                    while True:
                        print("Enter 0 to appear a test \n Press and enter any other key to go back")
                        back = input()
                        if back != "0" :
                            return
                        print("Enter test name:")
                        testname = input()
                        if path.isfile( (testname + ".pkl" ) ) :
                            ###Enter test sequence
                            print("\n Answer the following MCQ. Enter either of the four options (1,2,3,4) \n")
                            testfl=open ( (testname + ".pkl" ) , "rb" )
                            testdetails= pickle.load(testfl)
                            testfl.close()

                            usertest = {}
                            for key,value in testdetails.items() :
                                print( key,".  ",value[0])
                                
                                count = 0
                                for option in value[1] :
                                    count +=1
                                    print ( "(" , count ,")",option)

                                while True:
                                    print("Enter your answer")
                                    answer=input()
                                    if int(answer) in [1,2,3,4] :
                                        break
                                    else :
                                        print("Invalid option entered !!! Try again...")
                                usertest.update( { key : ( value[0] , value[1], value[2], int(answer) ) } )

                            user = open ( (username + ".pkl" ) , "wb" )
                            pickle.dump(usertest, user)  ###User test details
                            user.close()
                            break
   
                        else :
                            print(testname , " doesn't exists !!! Try again...")

                showresult(username)
                    
                
            else :
                print("Wrong Password !!! Try again....")
        else:
            print("User ",username, "doesn't exists !!!! Try again....")

           

def newadmin():
    print("\n")
    print("Enter Admin's username")
    username=input()
    print("Enter password")
    password=input()
    admins_file = open ( "admin.pkl" , "rb")
    admins_dict = pickle.load(admins_file)
    admins_file.close()
    admins_dict.update( {username : password } )
    admins_file = open ( "admin.pkl" , "wb")
    pickle.dump(admins_dict, admins_file)
    admins_file.close()
    null_acc = []
    admin = open ( ("admin_" + username + ".pkl" ) , "wb" )
    pickle.dump( null_acc , admin)
    admin.close()
    print("Admin ", username, "created successfully !!!")


def admin():
    print("\n")
    while True:
        print("Enter 0 to go back. \n To continue press any other key and enter.")
        back = input()
        if back == "0" :
            return
        print("Enter Admin's username")
        username=input()
        print("Enter password")
        password=input()
        admin_file = open ( "admin.pkl" , "rb")
        admin_dict = pickle.load(admin_file)
        admin_file.close()
        if username in admin_dict.keys():
            if admin_dict[username] == password :
                admin = open ( ("admin_" + username + ".pkl" ) , "rb" )
                tests = pickle.load(admin)
                admin.close()
                print("Welcome Admin ", username )
                ## Continue Admin create test sequence
                while True:
                    print("Enter 0 to create new test \n Press and enter any other key to log out")
                    back = input ()
                    if back != "0" :
                        break
                    print("Enter test's name")
                    testname = input()
                    ## Continued
                    tests.append(testname)
                    testfl=open ( (testname + ".pkl" ) , "wb" )
                    testdetails={}
                    count=0
                    while True:
                        print("Enter 0 to add a question \n Press and enter any other key to exit")
                        back = input()
                        if back != "0" :
                            break
                        
                        print("Enter question:-")
                        question = input()

                        options=[]
                        print ("Enter options :-")
                        for i in [1,2,3,4]:
                            print( "Option (",i,")")
                            tempopt =input ()
                            options.append(tempopt)

                        answer = "0"
                        while True:
                            print("Enter correct option no.")
                            answer = input()
                            if int(answer) in [1,2,3,4] :
                                break
                            print("Invalid option no. !!! Try again...")
                            
                        count += 1
                        testdetails.update( { count : [question, options , int(answer)] } )

                    pickle.dump(testdetails , testfl)
                    testfl.close()
                    print(testdetails)
                    
                admin = open ( ("admin_" + username + ".pkl" ) , "wb" )
                pickle.dump( tests , admin)
                admin.close()
                
            else :
                print("Wrong Password !!! Try again....")
        else:
            print("Admin ",username, "doesn't exists !!!! Try again....")



##########################################
##                    MAIN PROGRAM                       ##
##########################################

            
print("Welcome to QUIZ program")

if not path.isfile( "users.pkl"  ) :
    users = {}
    users_file = open("users.pkl", "wb")
    pickle.dump(users, users_file)
    users_file.close()

if not path.isfile( "admin.pkl"  ) :
    admin = {}
    admin_file = open("admin.pkl", "wb")
    pickle.dump(admin, admin_file)
    admin_file.close()


while True:
    print("Choose an option :- \n 1 : User \n 2 : Admin \n Enter :-")
    login_type = input()
    if login_type == "1":
        while True:
            print("Choose an option :- \n 1 : Log in  \n 2 : Create New User \n Enter :-")
            login = input()
            if login == "1":
                user()
            elif login == "2":
                newuser()
            else:
                print("Invalid option !!!! Try again.... ")
    elif login_type == "2":
        while True:
            print("Enter admin authentication code: ")
            code = input()
            if code == "777" :
                print("Welcome to admin portal")
                while True:
                    print("Choose an option :- \n 1 : Log in  \n 2 : Create New Admin \n Enter :-")
                    login = input()
                    if login == "1":
                        admin()
                    elif login == "2":
                        newadmin()
                    else:
                        print("Invalid option !!!! Try again.... ")
            else:
                print("Invalid authentication code !!!! Try again.... ")
    
    else:
        print("Invalid option !!!! Try again.... ")



       
