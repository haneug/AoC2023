def getnumber(line):
    ints = []
    start = 0
    counter = 0
    for i in line:
        counter += 1
        try:
            ints.append(int(i))
            start = counter
        except:
            tmp = line[start:counter]
            for number in numberlist:
                if number in tmp:
                    ints.append(int(dictnumbs[number]))
                    start = counter - 1
    return int(str(ints[0]) + str(ints[-1]))

numberlist = [ 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' ]
dictnumbs = {'one': 1, 'two': 2, 'three' : 3, 'four' : 4, 'five' : 5, 'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9}

file = open('input.txt','r')
lines = file.read().splitlines()
result = 0

for line in lines:
    number = getnumber(line)
    print(number)
    result += number
print(result)
    
