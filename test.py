

# 딕셔너리를 이용한 환율 변환 프로그램
# 환율 = {"달러": 1167, 
#         "엔": 1.096, 
#         "유로": 1268, 
#         "위안": 171}

# user = input("입력: ")
# num, currency = user.split()
# print(float(num) * 환율[currency], "원")

# 3개의 숫자를 입력받은 후 가장 큰 숫자 출력
# number = []

# for _ in range(3):
#     user_input = int(input("숫자 : "))
#     number.append(user_input)

# print(max(number))


# # 휴대전화 번호를 입력받고 통신사 알아내기
# user_input = input("입력 : ")
# number_list = user_input.split('-')

# if number_list[0] == "011":
#     com = "skt"
# elif number_list[0] == "016":
#     com = "kt"
# else:
#     com = "lg"

# print(f"{com}")


# 단어에서 특정 자릿수를 구해 일치하는지 측정
# post_number = input("입력 : ")
# post_number = post_number[:3]

# if post_number in ["010", "011", "012"]:
#     print("강북구")
# elif post_number in ["014", "015", "016"]:
#     print("도봉구")
# else:
#     print("노원구")


# number = input("주민 번호 : ")
# input_number = number.split("-")

# 남녀 판별
# if input_number[0] == "1" or input_number[0] == "3":
#     print("남자")
# else:
#     print("여자")

# 출생지 판별
# if 0 <= int(input_number[1:3]) <= 8:
#     print("서울")
# else:
#     print("서울이 아니다.")

#주민번호 유효성 판별
# number = input("주민 번호 : ")
# input_number = number.replace("-", "")
# number_list = list(input_number)

# last_number = 11 - ((int(number_list[0])*2 +int(number_list[1])*3 +int(number_list[2])*4 +int(number_list[3])*5 +int(number_list[4])*6 +int(number_list[5])*7 +int(number_list[6])*8 +int(number_list[7])*9+int(number_list[8])*2+int(number_list[9])*3+int(number_list[10])*4 +int(number_list[11])*5) % 11)

# if last_number == int(number_list[12]):
#     print("유효함")
# else:
#     print("유효하지 않습니다.")


# import requests
# # btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']   # 회사망에서 접근 안되는듯
# btc = {"opening_price":"49226000","closing_price":"48933000","min_price":"48366000","max_price":"50090000","units_traded":"4044.70721499","acc_trade_value":"198828899319.4815","prev_closing_price":"49218000","units_traded_24H":"5415.29547028","acc_trade_value_24H":"267049909774.077","fluctate_24H":"-1039000","fluctate_rate_24H":"-2.08","date":"1700632573150"}

# change_price = int(btc["max_price"])- int(btc["min_price"])
# result = int(btc["opening_price"]) + change_price

# if result > int(btc["max_price"]):
#     print("상승장")
# else:
#     print("하락장")

# # 리스트 슬라이싱
# 리스트 = ["가", "나", "다", "라"]
# for 변수 in 리스트[1:]:
#   print(변수)


# # 리스트의 첫번째 문자만 대문자로 변경 후 이어 붙여 출력
# 리스트 = ['dog', 'cat', 'parrot']

# for x in 리스트:
#     j = x[0].upper()
#     print(j + x[1:])


# 99 부터 0 까지 숫자를 거꾸로 출력할 때 빼기를 이용하지 않으면 0 은 출력할 수 없음
# for x in range(99, 0, -1):
#     print(x)

# for i in range(100):
#     print(99 - i)


#  소수점 출력을 원할 때 나누기를 이용
# for num in range(10) :
#     print(num / 10)


# price_list = [32100, 32150, 32000, 32500]

# # list 의 개수가 변해도 계속 사용할 수 있는 함수
# for i in range(len(price_list)):
#     print(price_list[i])
    
# enumerate 는 리스트의 데이터를 보여줌
# for i, data in enumerate(price_list):
#     print(i, data)

# for i in range(len(price_list)):
#     print((len(price_list)-1)- i, price_list[i])

# for i in range(1, 4):
#     print(90 + 10 * i, price_list[i])


# my_list = ["가", "나", "다", "라"]

# # 아래 3개는 모두 동일한 값을 출력
# for i in [0, 1, 2]:
#     print(my_list[i], my_list[i+1])
    
# for i in range(len(my_list) - 1 ) :
#   print(my_list[i], my_list[i+1])

# for i in range( 1, len(my_list) ) :
#   print(my_list[i-1], my_list[i])


# my_list = ["가", "나", "다", "라", "마"]

# for i in range( 1, len(my_list)-1 ) :
#   print(my_list[i-1], my_list[i], my_list[i+1])

# my_list = ["가", "나", "다", "라"]

# for i in range(len(my_list), 1, -1):
#     print(my_list[i-1], my_list[i-2])


# # abs 함수는 무조건 양수를 반환
# my_list = [100, 200, 400, 800]

# for i in range(len(my_list) - 1):
#     print(abs(my_list[i+1] - my_list[i]))


# 3일 이동 평균을 계산하고 이를 화면에 출력
# my_list = [100, 200, 400, 800, 1000, 1300]

# for i in range(1, len(my_list)-1):
#     print(float((my_list[i-1] + my_list[i] + my_list[i+1])/3))



# low_prices  = [100, 200, 400, 800, 1000]
# high_prices = [150, 300, 430, 880, 1000]

# volatility = []

# for i in range(5):
#     vol = high_prices[i] - low_prices[i]
#     volatility.append(vol)

# print(volatility)


# # 리스트 거꾸로 돌려 순서대로 출력
# apart = [[101, 102],[201, 202],[301, 302]]

# for row in apart[::-1]:
#     for col in row[::-1]:
#         print(col)


# 이중 리스트 배열 저장
# data = [
#     [ 2000,  3050,  2050,  1980],
#     [ 7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]

# result = [
# ]

# for row in data:
#     sub = []
#     for col in row:
#         sub.append(col * 1.00014)
#     result.append(sub)
# print(result)




