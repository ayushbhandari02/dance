string1=' i will keep dancing '
string1=string1.title()
print(string1)
string2='i will stop dancing'
string3='my age is {0} and born in {1}'
string2=string2.title()
print(string2)
print(string1+' '+string2)
for i in range(-1, -20, -1):
    print(string1[i])
print(string1.strip())
print(string1[0:4])
print(len(string1))
print(string1.upper())
print(string1.replace("i","w"))
print(string1.split(" "))
print(string3.format(23,1995))


