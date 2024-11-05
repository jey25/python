def calculator(a, b, operator):
    if operator == "+":
        return a+b
    else:
        return a-b

# 사용 예시
print(calculator(5, 3, "+"))  # 출력: 8
print(calculator(5, 2, "-"))  # 출력: 2