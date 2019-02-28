howFar = int(input("What sequence number are we going up to? Tell me: "))
x = 0
fibonacci = 0
oldValue = 1

while x < howFar:
    print(fibonacci)
    sum = fibonacci + oldValue
    fibonacci = oldValue
    oldValue = sum
    x += 1