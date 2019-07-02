while (1):
    print("\n1.addition\n2.subtraction\n3.multiplication\n4.division\n5.power exponential\n6.exit")


    def add(sel1, sel2):
        return (sel1 + sel2)


    def sub(sel1, sel2):
        return (sel1 - sel2)


    def mul(sel1, sel2):
        return (sel1 * sel2)


    def div(sel1, sel2):
        try:
            return (sel1 / sel2)
        except ZeroDivisionError:
            print("0 in the denominator")


    def pow(sel1, sel2):
        return (sel1 ** sel2)


    sel = 0
    try:
        sel = int(input("Please select the operation you want to perform"))
    except ValueError:
        print("only integer value to be taken")
        exit()
    if sel == 6:
        exit()
    try:
        sel1 = int(input("enter the 1st operators"))
    except ValueError:
        print("only integer value to be taken")
        exit()
    try:
        sel2 = int(input("enter the 2nd operators"))
    except ValueError:
        print("only integer value to be taken")
        exit()

    if sel == 1:
        res = add(sel1, sel2)
    elif sel == 2:
        res = sub(sel1, sel2)
    elif sel == 3:
        res = mul(sel1, sel2)
    elif sel == 4:
        # res = 0
        res = div(sel1, sel2)
    elif sel == 5:
        res = pow(sel1, sel2)

    else:
        res = sel
    print(res)
