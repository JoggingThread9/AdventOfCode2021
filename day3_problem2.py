with open("day3_data.rtf") as f:
    data = [x for x in f.read().split()]

oxygen = 0
co2 = 0
life_support = oxygen * co2

zero = 0
one = 0

loop = 0

for i in range(0,len(data[0])):
    zero = 0
    one = 0
    for j in range(0, len(data)):
        if data[j][i] == "0":
            zero += 1
        else:
            one += 1
    for k in data[:]:
        if zero > one:
            if k[i] == "1":
                data.remove(k)
        else:
            if k[i] == "0":
                data.remove(k)

for i in data:
    print(i)
    x = i

with open("day3_data.rtf") as f:
    data = [x for x in f.read().split()]

for i in range(0,len(data[0])):
    zero = 0
    one = 0
    for j in range(0, len(data)):
        if data[j][i] == "0":
            zero += 1
        else:
            one += 1
    for k in data[:]:
        if zero < one:
            if k[i] != "1":
                data.remove(k)
        else:
            if k[i] != "0":
                data.remove(k)

for i in data:
    print(i)
    y = i

print(1157 * 1160)