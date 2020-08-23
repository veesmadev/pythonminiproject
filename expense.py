import pickle

def addexp():
    while True:
        print("Choose an option....\n 1 : Add Expense \n 0: Quit \n Enter:-")
        option=input()
        if option== "1":
            print("Enter expense type-")
            key=input()
            print("Enter expense amount-")
            value=input()
            print("Entered expense:   ", key, "=" , value, "/-")
            exp_file = open("data.pkl", "rb")
            expense=pickle.load(exp_file)
            exp_file.close()
            exp_file = open("data.pkl", "wb")
            temp=0
            if key in list(expense.keys()):
                temp = expense[key]
                temp=int(value)+temp
                expense[key]=temp
            else:
                expense.update({key : int(value) })
            pickle.dump(expense, exp_file)
            exp_file.close()
            print("Expense added successfully\n")

        elif option == "0":
            return
        else:
            print("Invalid option entered !!!  Try Again.....")

def showexp():
    print("\n")
    print("="*40)
    print("Expenditure Report:-")
    print("="*40)
    exp_file = open("data.pkl", "rb")
    expense = pickle.load(exp_file)
    total=0
    for value in expense.values():
        total=total + value;
    for key, value in sorted(expense.items(), key=lambda x: x[1], reverse=True):
        print(key, "  =  ", value, "/-        (  %.2f" % (100*value/total), "% )")
        
    print("="*40)
    print("Total Expenditure = ", total, "/-")
    print("="*40)
    exp_file.close()


##########################################
##                    MAIN PROGRAM                       ##
##########################################


print("Welcome to Expense tracker Program")

try:
    exp_file = open("data.pkl", "rb")
    output = pickle.load(exp_file)
    print(output)

except EOFError : 
    expense = {}
    exp_file = open("data.pkl", "wb")
    pickle.dump(expense, exp_file)
    exp_file.close()
    exp_file = open("data.pkl", "rb")
    output = pickle.load(exp_file)
    print(output)
    
while True:
      print("\n\nSelect an option .....\n 1 : Add expense \n 2 : Show Expense Report \n Enter :- ")
      option= input()    
      if option=="1":
          addexp()
          print(option)
      elif option == "2":
          showexp()
      else:
          print("Invalid option entered !!!  Try Again.....")

      
