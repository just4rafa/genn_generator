import random 


# Creating gen number
def rand_numb():
    numbers = [1,2,3,4,5,6,7,8,9]
    global num
    numg = random.choice(numbers) + random.choice(numbers) + random.choice(numbers)
    numc = numg * random.choice(numbers)
    num = numc
       
rand_numb()


# Creating gen generators 
def gen1(n):
    """A random number resulted from the gathering of two random numbers + gen numb
    
    Returns:
        int: An integer number, from -? to +?
    """
    numbers = [1,2,3,4,5,6,7,8,9]
    numb = random.choice(numbers) + random.choice(numbers)
    gen = n + numb
    return 'YOUR NUMBER IS ' + str(gen)

def gen2(n):
    """A random number resulted from the substraction of two random numbers + gen numb
    
    Returns:
        int: An integer number, from -? to +?
    """
    numbers = [1,2,3,4,5,6,7,8,9]
    numb = random.choice(numbers) - random.choice(numbers)
    gen = n - numb
    return 'YOUR NUMBER IS ' + str(gen)

def gen3(n):
    """A random number resulted from the multiplication of two random numbers * gen numb
    
    Returns:
        int: An integer number, from -? to +?
    """
    numbers = [1,2,3,4,5,6,7,8,9]
    numb = random.choice(numbers) * random.choice(numbers)
    gen = n * numb
    return 'YOUR NUMBER IS ' + str(gen)

def gen4(n):
    """A random number resulted from the division of two random numbers / gen numb
    
    Returns:
        int: An integer number, from -? to +?
    """
    numbers = [1,2,3,4,5,6,7,8,9]
    numb = random.choice(numbers) / random.choice(numbers)
    gen = n / numb
    return 'YOUR NUMBER IS ' + str(round(gen))

def gen5(n):
    """A random number resulted from the power of two random numbers * gen numb
    
    Returns:
        int: An integer number, from -? to +?
    """
    numbers = [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,75,80,85,90,95]
    power = random.choice(numbers)
    genn = n ** power
    x = True
    while x == True:
        if genn > 2000000000000000 < 200000000000000000000000000000:
            genn = n ** power
            x = False
        else:
            genn = n ** power
            x = True
    gen = genn
    return 'YOUR NUMBER IS ' + str(gen)

def gen6(n):
    """A random number resulted from the power of two random numbers * gen numb
    
    MORE BIGGER NUMBERS
    
    Returns:
        int: An integer number, from -? to +?
    """
    numbers = [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,75,80,85,90,95]
    power = random.choice(numbers)
    # The power for for while
    power1 = random.choice(numbers)
    # The gen number for while
    genn = n ** power
    x = True
    while x == True:
        numbers = [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,75,80,85,90,95]
        numbers = random.shuffle(numbers)
        numbersl = [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,75,80,85,90,95]
        numbers = random.shuffle(numbersl)
        power1 = random.choice(numbersl)
        power = power1
        if genn > 90000000000000000000000000000000000000000000:
            genn = n ** power
            x = False
        else:
            genn = n ** power
            numbers = [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,75,80,85,90,95]
            numbers = random.shuffle(numbers)
            numbersl = [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,75,80,85,90,95]
            numbers = random.shuffle(numbersl)
            power1 = random.choice(numbersl)
            power = power1
            x = True
    gen = genn
    return 'YOUR NUMBER IS ' + str(gen)


# Creating user display and commnads
def input_user():
    def welcome_screen():
        print("Welcome to gen number generator, created by Rafa")
        print()
        print("A simple program that generates random numbers that depends on your choice.")
        print()
        print("NOTE that the number resulted from the division is rounded!")
        print()
        print()
    welcome_screen()
    usrinp = ''
    while usrinp != 'quit':
        rand_numb()
        print()
        print("A new gen number is generated!")
        print(f'Your gen number is {num}')
        comm_user = input("""
quit - to quit
gen1 - addition
gen2 - substraction
gen3 - multiplication
gen4 - division
gen5 - power
gen6 - x3 power
commnad: """) 
        # Commands checking
        if comm_user == 'gen1':
            print()
            print(gen1(num))
        if comm_user == 'gen2':
            print()
            print(gen2(num))
        if comm_user == 'gen3':
            print()
            print(gen3(num))
        if comm_user == 'gen4':
            print()
            print(gen4(num))
        if comm_user == 'gen5':
            print()
            print(gen5(num))
        if comm_user == 'gen6':
            print()
            print(gen6(num))
            
        # Creating quit method
        if comm_user == 'quit':
            usrinp = 'quit'
            print()
            print("Goodbye")
    
    
input_user()