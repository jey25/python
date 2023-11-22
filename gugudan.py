
result = []

def GuGu(n):
    i = 1
    while i < 10:
        result.append(n*i)
        i += 1    
    return result

GuGu(3)

for number in result:
    print(str(number))

