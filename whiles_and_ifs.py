



#%%


price = 1000000
has_good_credit = True
if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")


has_criminal_record = True
has_good_credit = True

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
    
    
temperature = 35
if temperature > 30:
    print("it's a hot day")
else:
    print("its not a hot day")


name = "Fatima"
if len(name) < 3:
    print("name must be at least 3 characters")
elif len(name) >  50:
    print("name must be a maximum of 50 characters")
else:
    print("name looks good")



weight: 160

weight = int(input('Weight: '))
unit = input('(L)bs or k(g): ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"you are {converted} kilos")
else:
    converted = weight / 0.45
    print(f" you are {converted} pounds")
    


secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break
else:
    print("Sorry you lost1!")
 
    
command = ""
while command.upper != "quit": 
     command =input("> ")
     if command == "start":
         print ("car started...")
     elif command == "stop":
         print("car stopped")
     elif command == "help":
         print("""
start - to start the car
stop - to stop the car
quit - to quit
               """)
     elif command == "quit":
      break
     else:
         print("sorry, I dont understand that command")
         
    
    


    
    







































