

user = input("입력 : ")
result = user - 20

if result > 255:
    print(255)
elif result < 0:
    print(0)
else:
    print(result)