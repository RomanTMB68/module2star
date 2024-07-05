def key(n):
    result = ""
    for i in range(1, n):
        for g in range (i+1, n+1):
            if n % (i+g) == 0:
                result += str(i) + str(g)
    return result


for n in range (3, 21):
    result = key(n)
    print (f"{n} - {result}")
