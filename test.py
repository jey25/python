

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


# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# 함수 (201 번 문제 ~)

# def print_arithmetic_operation(x, y):
#     print(f"{x} + {y} = {x + y}")
#     print(f"{x} - {y} = {x - y}")
#     print(f"{x} * {y} = {x * y}")
#     print(f"{x} / {y} = {x / y}")

# print_arithmetic_operation(3,4)


# def print_max(x, y, z):
#     if x > y:
#         if x > z:
#             print(x)
#         else:
#             print(z)
#     elif y > z:
#         print(y)
#     else:
#         print(z)

# def print_max(a, b, c) :
#     max_val = 0
#     if a > max_val :
#         max_val = a
#     if b > max_val :
#         max_val = b
#     if c > max_val :
#         max_val = c
#     print(max_val)

# print_max(265,0,19)


# 10000 미만의 자연수에서 4의 배수와 7의 배수의 총합 구하기

# result = 0
# for i in range(1, 10000):
#     if i % 4 == 0 or i % 7 == 0:
#         result += i

# print(result)


# #구구단
# result = []

# def GuGu(n):
#     i = 1
#     while i < 10:
#         result.append(n*i)
#         i += 1    
#     return result

# GuGu(6)

# for number in result:
#     print(number)


# # 로또 번호 추출
# import random

# lotto = sorted(random.sample(range(1,46), 6))
# print(lotto)


# 문자열 역순 출력
# def print_reverse(str):
#     print(str[::-1]) 
    
# print_reverse("python")


# # 리스트를 받아 평균 출력
# def print_score(list):
#     print(sum(list)/len(list))

# print_score ([1, 2, 3])


# # dict 에서 키값만 출력
# def print_keys(dict):
#     for i in dict.keys():
#         print(i)

# print_keys({"이름":"김말똥", "나이":30, "성별":0})


# # key 를 입력받아 value 출력
# my_dict = {"10/26" : [100, 130, 100, 100],
#            "10/27" : [10, 12, 10, 11]}

# def print_value_by_key(dict, days):
#     print(dict[days])

# print_value_by_key  (my_dict, "10/27")


# # # 입력 문자를 한 줄에 다섯글자씩 출력
# def print_5xn(line):
#     chunk_num = int(len(line) / 5)
#     for x in range(chunk_num + 1) :
#         print(line[x * 5: x * 5 + 5])

# print_5xn("아이엠어보이유알어걸")

#여러 인수를 갖는 함수
# def add(*args):
#     i = 0
#     for n in args:
#         i += n
#     return i

# print(add(3, 5, 7,8, 12, 23, 4 , 65))


# def n_plus_1 (n) :
#     result = n + 1
#     return result

# print(n_plus_1(3))


# # replace 는 인텔리센스 자동완성 제공되지 않음
# def convert_int(str):
#     t = str.replace(',', '')
#     print(type(t))
#     s = int(t)
#     print(type(s))
#     return s

# print(convert_int("1,234,567"))

# # 현재 시간 출력
import datetime
import time
# print(datetime.datetime.now())
# print(type(datetime.datetime.now()))

# 과거 날짜 출력
# now = datetime.datetime.now()

# for day in range(5, 0, -1):
#     delta = datetime.timedelta(days=day)
#     date = now - delta
#     print(date)

# 2023-12-19 14:40:22 형태로 출력 
# now = datetime.datetime.now()
# log_time = now.strftime("%Y-%m-%d %H:%M:%S")
# print(log_time)

# # 문자열을 시간 값으로 변경
# day = "2020-05-04"
# ret = datetime.datetime.strptime(day, "%Y-%m-%d")
# print(ret, type(ret))

# # 1초에 한번씩 현재 시간 출력
# while True:
#     now = datetime.datetime.now()
#     now_time = now.strftime("%H:%M:%S")
#     print(now_time)
#     time.sleep(1)


# # 현재 경로 출력
# import os
# ret = os.getcwd()
# print(ret, type(ret))

# # 바탕화면 파일 이름 변경
# os.rename(r"C:\Users\eyjang\Desktop\test.txt", r"C:\Users\eyjang\Desktop\test1.txt")


# import numpy
# # numpy 로 0.1 씩 증가하는 값 출력
# for i in numpy.arange(0, 5, 0.1):
#     print(i)


# python 클래스 인스턴스
# class Human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
        
#     def __del__(self):
#         print("나의 죽음을 알리지마라")
    
#     def who(self):
#         print(self.name, self.age, self.sex)
    
#     def setInfo(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex

# areum = Human("불명", "미상", "모름")
# areum.who()      # Human.who(areum)

# areum.setInfo("아름", 25, "여자")
# areum.who()      # Human.who(areum)

# del areum


# 클래스 안의 메서드에는 self 가 항상 존재해야 함
# class OMG:
#     def print(self):
#         print("Oh my god")

# # 클래스의 인스턴스를 생성
# myStock = OMG()

# # 메서드 호출
# myStock.print()


# Stock 클래스의 객체가 생성될 때 종목명과 종목코드를 입력 받을 수 있도록 생성자를 정의
# class stock:
#     def __init__(self, key, code):
#         self.key = key
#         self.code = code
        
#     def set_name(self, name):
#         self.key = name
        
#     def set_code(self, code):
#         self.code = code
    
#     def get_name(self):
#         return self.key

#     def get_code(self):
#         return self.code


# 삼성 = stock("삼성전자", "005930")
# print(삼성.key)
# print(삼성.code)
# print(삼성.get_name())
# print(삼성.get_code())




