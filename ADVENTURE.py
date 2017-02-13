print("your side of the story...")

person1 = raw_input("what is your name")

print("press enter to tell your story side of the story")

print('''you are in your office, is late at night. the problem is that you 
are the last one in the office, or at least that is what you thought...
do you check it out? or do you keep working?.''')
#if choise = check it out or keep working
choice = raw_input()
if choice == "check it out":
    print("nothing showed up")
    print("but something moved")
elif choice == "keep investigating":
    if(raw_input("shout out at the moving object, and see if it responds(type shout)") == 'shout'):
    	print("you felt a bad force surrounding you")
    else: 
    	print("you get pushed by an unknown force")

        choice = raw_input()

        if choice == "stand up and run to the exit door":
            print("trip in the stairs on your way out")
elif choice == "keep working": 
    print("you heared a scream")
    print("you got scared")
    choice = raw_input()
    if choice == "call the cops":
    	print("no signal in the building")
