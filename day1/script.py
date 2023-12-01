def getnumber(line):
    ints = []
    for i in line:
        try:
            ints.append(int(i))
        except:
            continue
    return int(str(ints[0]) + str(ints[-1]))


file = open('input.txt','r')
lines = file.read().splitlines()
result = 0

for line in lines:
    number = getnumber(line)
    #print(number)
    result += number
print(result)
    
