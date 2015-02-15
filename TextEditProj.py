# Simple text program to explore using GitHub
com_num = 0
page = ["","","","","","","","","",""]
# Error check --------------------------
def errorchk(com):
    if (len(com) > 1):
        if (com[1].isdigit()):
            line = int(com[1])
            if ((line >=0) & (line <= 9)):
                return 1
            else: print "Line range 0 - 9"
        else: print "Command argument must be 0-9"    
        
    else: print "Command requires argument 0-9"
    return 0

# Print Lines of Text ------------------
def pageout():
    print "# |----1----2----3----4----5----6----7----8"
    for i in range(10):
        j = str(i)
        print j + " |" + page[i]

# Write a string to line 0 to 9 --------
def linewrite(l):
    print "Enter a line of text for line {0}.\n".format(l)
    line = raw_input("->")
    l = int(l)
    page[l] = line

# Justify left -------------------------
def justleft(l):
    l = int(l)
    page[l] = page[l].lstrip()
# Justify right ------------------------    
def rightjust(l):
    l = int(l)
    page[l] = page[l].rstrip()
    page[l] = page[l].rjust(40)
# Count instances of a string ----------
def textcount(t):
    current_count = 0
    line_count = 0
    for i in range(10):
        line_count = page[i].count(t)
        current_count = current_count + line_count
    return current_count
# write to all 10 lines ----------------
def writeall():
    print "Type up to 40 character per line"
    for j in range(10):
        k = str(j)
        line = raw_input("line "+ k + " ->")
        page[j] = line
    
# Print help page --------------------
def helppage():
    print """
    Instructions.
    1. print : print current contents of page.
    2. write 0-9 : write text to line 0-9.
    3. ljust 0-9 : left justify line 0-9.   
    4. rjust 0-9 : right justify line 0-9.
    5. count 'string' : will count instances of 'string'
                        in text.
    6. writeall : write 10 lines of text 0-9.                    
    8. help : will display commands.
    9. exit : will exit from program.
    
    """

print "Welcome to Aaron's text Editor"
helppage()
while (com_num != 9):
    command = raw_input("enter command ->")
    command = command.split()
    
    if (command[0] == "print") or (command[0] == "1"):
        pageout()
    
    elif (command[0] == "write") or (command[0] == "2"):
        if (errorchk(command)):
            linewrite(command[1])
            
    elif (command[0] == "ljust") or (command[0] == "3"):
        if (errorchk(command)):
            justleft(command[1])
    
    elif (command[0] == "rjust") or (command[0] == "4"):
        if (errorchk(command)):
            rightjust(command[1])
    
    elif (command[0] == "count") or (command[0] == "5"):
        total = 0
        if (len(command) > 1):
            total = textcount(command[1])
            print "Total count for '{0}' is {1}.".format(command[1], total)
        else: print "Command needs a string as an arguement."
        
    elif (command[0] == "writeall") or (command[0] == "6"):
        writeall()
        
    elif (command[0] == "help") or (command[0] == "8"):
        helppage()
    
    elif ((command[0] == "9") or (command[0] == "exit")):
        print "Good bye."
        com_num = 9

