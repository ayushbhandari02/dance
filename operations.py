
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
import platform
x=platform.system()
print(x)
y=dir(platform)
print(y)
import datetime
a=datetime.datetime(2019,5,4)
print(a)


