
# 10000 미만의 자연수에서 4의 배수와 7의 배수의 총합 구하기

result = 0
for i in range(1, 10000):
    if i % 4 == 0 or i % 7 == 0:
        result += i


print(result)