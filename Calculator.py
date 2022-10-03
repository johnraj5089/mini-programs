import os 
print('''           _            _       _             
          | |          | |     | |            
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                              ''')
def addition (a,b):
  return a+b
def subtract(a,b):
  return a-b
def multiply(a,b):
  return a*b
def division(a,b):
  return a/b
cont = True
num1= float(input("what is the first Number? "))
while cont:
  oper = input("+\n-\n*\n/\nPick an operation: ")
  num2= float(input("what is the Next Number? "))
  if oper == '+': # can use a dictionay for this which can minimize the code 
    ans = addition(num1,num2)
    print (f"{num1} {oper} {num2} = {ans}")
  elif oper == '-':
    ans = subtract(num1,num2)
    print (f"{num1} {oper} {num2} = {ans}")
  elif oper == '*':
    ans = multiply(num1,num2)
    print (f"{num1} {oper} {num2} = {ans}")
  elif oper == '/':
    ans = division(num1,num2)
    print (f"{num1} {oper} {num2} = {ans}")
  else:
    print("Invalid operator")
  num1 = ans
  choice = input (f"Type 'y' to continue calculating with {ans}, or 'n' to start a new calculation : " ).lower()
  if choice == 'n':
    os.system('cls')
    num1= float(input("what is the first Number? "))
  elif choice == 'y':
    pass
  else:
    print("invalid choice.")
    cont = False
