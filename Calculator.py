
con = True
forans = 0

def perfops():
    global con
    global forans

    if  forans == 0:
        eqtn = input('Enter equation:')
        if not(eqtn == 'quit'):
            eqtn = eval(eqtn)
            print(eqtn)
            forans = eqtn
            return()
        elif (eqtn == 'quit'):
            con = False
            return()
    else:
        print(forans,)
        eqtn = input()
        if(eqtn == 'quit'):
            con =False
            return()
        forans = str(forans) + eqtn
        forans = eval(forans)
        forans = round(forans , 3)



print('CALCULATOR FOR SIMPLE EQUATION OPERATIONS')
while con:
    perfops()