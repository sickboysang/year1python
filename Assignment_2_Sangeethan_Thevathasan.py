Final = "Final save "
storage = 0
while True:
    op = input(" would you like to add, subtract, multiply, divide, or raise (exponents) two floats: ")
    if op == "stop" or op == "exit":
        break
    num_one = input("Enter number 1 : ")
    if num_one == "stop" or op == "exit":3
        break
    if(num_one == ""):
        num_one = storage
    num_two = input("Enter a number 2 : ")
    if num_two == "stop" or op == "exit":
        break
    if (num_two == ""):
        num_two = storage
    if (op == "*" or op=="Multiply"  ):
        multi = float(num_one)* float(num_two)
        Final = multi
        storage = Final
    elif (op == "+" or op=="add" ):
        add = float(num_one)+float(num_two)
        Final = add
        storage = Final
    elif (op == subtract"-" or op =="subtract" ):
         = (float(num_one)) - (float(num_two))
        Final = subtract
        storage = Final
    elif (op == "/" or op=="divide" ):
        div = (float(num_one))/(float(num_two))
        Final = div
        storage = Final
    elif (op == "**" or op=="exponet" ) :
        exp = 1
        num_two = float(num_two)
        for i in range(0,num_two):
            exp = exp*num_one
        Final = exp
        storage = Final
    else:
        print("Invalid")
    print(Final)
print("The code is working through the Code")

