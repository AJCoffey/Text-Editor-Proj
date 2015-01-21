# Simple text program to explore using GitHub
com_num = 0
page = ["","","","","","","","","",""]

def pageout():
    print "# |----1----2----3----4----5----6----7----8"
    for i in range(10):
        j = str(i)
        print j + " |" + page[i]
        
while (com_num != 9):
    command = raw_input("enter command ->")
    if (command == "print"):
        pageout()
    elif ((command == "quit") or (command == "exit")):
        com_num = 9

