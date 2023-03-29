palind = 0
number = ""
count = 0
for x in range(10,100):
    for y in range(10,100):
        number = str(x*y)
        if number == number[::-1]:
            palind = int(number)
print(palind)