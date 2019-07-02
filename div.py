def div(sel1, sel2):
    try:
        return (sel1 / sel2)
    except ZeroDivisionError:
        print("0 in the denominator")