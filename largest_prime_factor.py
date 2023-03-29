number = 600851475143
largest_prime = 0
count = 0
for x in range(2,number + 1):
    if (number % x == 0):
        for y in range(2,x):
            if x % y == 0:
                count += 1
            else:
                pass
        print(x,count)
        if count == 0:
            largest_prime = x
    count = 0

print(largest_prime)