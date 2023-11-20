
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
t_list = []

for warn in warn_investment_list:
    t= warn.lower()
    t_list.append(t)

user_input= input("입력 : ").lower()

if user_input in t_list:
    print("투자 경고")
else:
    print("정답")
