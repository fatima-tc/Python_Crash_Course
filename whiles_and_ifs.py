

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
 
#%%    
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
         
#%% 

for item in range(5, 10):
    print(item)
    
#%%
    prices = [10, 20, 30]
    
    total = 0
    for price in prices:
        total += price
    print(f"Total: {total}")
           
    
#%%
   
    for x in range(4):
        for y in range(3):
            print(f'({x}, {y})')
#%%
            numbers = [5, 2, 5, 2, 2]
            
            for item in numbers: 
                print('x' * item)
                
#%%
                names =[ 'John', 'Bob', 'Mosh', 'Sarah', 'Mary']
                names[0] = 'Jon'
                print(names[0:])
                print(names)
                
#%%  #finding max number in list
                
                numbers = [3, 6, 2, 8, 10]
                max = numbers[0]
                for number in numbers:
                    if number > max:
                        max = number
                print(max)
            
            
#%% #2D list
    

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][1])


#%%

numbers = [5, 2, 1, 7, 4]
numbers.pop()
print(numbers)


#%%
 #Tuples
numbers = (1, 2, 3)
print(numbers[0])
    


#%%
 
 #unpacking #tuples #lists
 
coordinates =[1, 2, 3]
x, y, z = coordinates
print(z)
 
 #%%
 #Dictionaires in Python

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
customer["birthdate"] = "April 25 1990"
print(customer["birthdate"])
 
#%%

phone = input("Phone: ")
digits_mapping = {
    "1": "one", 
    "2": "two",
    "3": "three",
    "4": "four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)

#%%
#emojis

message = input(">")
words = message.split(' ')
emojis = {
    ":)": "😁",
    ":(": "🙁"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
    print(output)
    
#%% #functions

def greet_user(): 
    print('Hi there!')
    print('Welcome aboard')


print("Start")
greet_user
print("Finish")

#%% #Parameters

def greet_user(name): 
    print(f'Hi {name}!')
    print('Welcome aboard')


print("Start")
greet_user("John")
print("Finish")


    



































