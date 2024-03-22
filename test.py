

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
from typing import Any
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


# class Stock:
#     def __init__(self, name, code):
#         self.name = name
#         self.code = code
    
#     def set_name(self, name):
#         self.name = name

# # 클래스를 변수에 넣을 때 꼭 None 값 입력해줘야 함 
# a = Stock(None, None)
# a.set_name("jey")

# print(a.name)


# class Stock:
#     def __init__(self, name, code, per, pbr, dividend):
#         self.name = name
#         self.code = code
#         self.per = per
#         self.pbr = pbr
#         self.dividend = dividend

#     def set_name(self, name):
#         self.name = name

#     def set_code(self, code):
#         self.code = code

#     def get_name(self):
#         return self.name

#     def get_code(self):
#         return self.code

#     def set_per(self, per):
#         self.per = per

#     def set_pbr(self, pbr):
#         self.pbr = pbr

#     def set_dividend(self, dividend):
#         self.dividend = dividend

# 삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
# 현대 = Stock("현대전자", "023430", 8.79, 0.33, 4.83)
# LG = Stock("LG", "005234", 315.79, 1.63, 1.83)

# s_list = [삼성, 현대, LG]

# for i in s_list:
#     print(i.code, i.per)


# 은행 계좌 개설 클래스
# import random

# class Account:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)

#         num1 = str(num1).zfill(3)      # 1 -> '1' -> '001'
#         num2 = str(num2).zfill(2)      # 1 -> '1' -> '01'
#         num3 = str(num3).zfill(6)      # 1 -> '1' -> '0000001'
#         self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001

# kim = Account("김민수", 100)
# print(kim.name)
# print(kim.balance)
# print(kim.bank)
# print(kim.account_number)


# import random

# class Account:
#     # class variable
#     account_count = 0

#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"

#         # 3-2-6
#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)

#         num1 = str(num1).zfill(3)      # 1 -> '1' -> '001'
#         num2 = str(num2).zfill(2)      # 1 -> '1' -> '01'
#         num3 = str(num3).zfill(6)      # 1 -> '1' -> '0000001'
#         self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
#         Account.account_count +=1

#     @classmethod
#     def get_account_num(cls):
#         print(cls.account_count)     # Account.account_count

#     def deposit(self, amount):
#         if amount >= 1:
#             self.balance += amount

# jang = Account("jang", 100)
# print(jang.balance)

# 45월 계좌에 입금
# jang.deposit(45)
# print(jang.balance)



# def display_info(self):
#     print("은행이름: ", self.bank)
#     print("예금주: ", self.name)
#     print("계좌번호: ", self.account_number)
    
#     # 포맷팅  :, 을 이용해서 천 단위 자리마다 쉼표를 찍는다
#     print("잔고: ", f"{self.balance:,}")

# p = Account("파이썬", 1000000000)
# p.display_info()


# 입금 횟수가 5회가 될 때 잔고를 기준으로 1%의 이자가 잔고에 추가되도록 코드를 변경해보세요.

# def deposit(self, amount):
#     if amount >= 1:
#         self.balance += amount

#         self.deposit_count += 1
#         if self.deposit_count % 5 == 0:         # 5, 10, 15
#             # 이자 지금
#             self.balance = (self.balance * 1.01)


# 클래스 상속
# class 차:
#     def __init__(self, 바퀴, 가격):
#         self.바퀴 = 바퀴
#         self.가격 = 가격

# class 자전차(차):
#     def __init__(self, 바퀴, 가격, 구동계):
#         super().__init__(바퀴, 가격)
#         self.구동계 = 구동계

# bicycle = 자전차(2, 100, "시마노")
# print(bicycle.구동계)
# print(bicycle.바퀴)
# print(bicycle.가격)


# # 부모 생성자 호출
# class 부모:
#   def __init__(self):
#     print("부모생성")

# class 자식(부모):
#   def __init__(self):
#     print("자식생성")
#     super().__init__()

# 나 = 자식()


# # 예외 처리 
# per = ["10.31", "", "8.00"]

# for i in per:
#     try:
#         print(float(i))
#     except:
#         print(0)


# per = ["10.31", "", "8.00"]
# new_per = []

# for i in per:
#     try:
#         v = float(i)
#     except:
#         v = 0
#     new_per.append(v)

# print(new_per)


# # list 인덱싱 에러
# data = [1, 2, 3]

# for i in range(5):
#     try:
#         print(data[i])
#     except IndexError as e:
#         print(e)


# per = ["10.31", "", "8.00"]

# for i in per:
#     try:
#         print(float(i))
#     except:
#         print(0)
#     else:
#         print("clean data")
#     finally:
#         print("변환 완료")


# # 별찍기 코드
# def star():
#     print("*" * 30)
#     print("")
#     print("*" * 30)

# star()

# num_str = "720"
# num_int = int(num_str)
# print(num_int+1, type(num_int))

# letters = 'python'
# print(letters[0], letters[2])


# license_plate = "24가 2210"

# # 아래 두 print 결과는 같다
# print(license_plate[4:])
# print(license_plate[-4:])


# string = "홀짝홀짝홀짝"

# # # 시작인덱스:끝인덱스:오프셋
# print(string[::2])  #홀홀홀
# print(string[1::2]) #짝짝짝


# string = "PYTHON"
# print(string[::-1]) #마지막 글자부터 순차적으로 출력  


# phone_number = "010-1111-2222"
# print(phone_number.replace("-", " "))
# print(phone_number.replace("-", ""))


# url = "http://sharebook.kr"

# print(url[-2::])

# url_split = url.split('.')
# print(url_split[-1])


# string = 'abcdfe2a354a32a'
# print(string.replace('a', 'A'))


# string = 'abcd'
# l = string.replace('b', 'B')
# print(l)


# t1 = 'python'
# t2 = 'java'

# print((t1 + " " + t2 + " ") * 4) 


# 상장주식수 = "5,969,782,550"
# print(int(상장주식수.replace(',', '')), type(int(상장주식수.replace(',', ''))))


# 분기 = "2020/03(E) (IFRS연결)"
# print(분기[:7])


# data = "   삼성전자    "
# data1 = data.strip()
# print(data)
# print(data.strip())
# print(data1)


# ticker = "btc_krw"
# print(ticker.upper())
# print(ticker)


# file_name = "보고서.xlsx"
# print(file_name.endswith("xlsx"))

# file_name = "보고서.xlsx"
# print(file_name.endswith(("xlsx", "xls")))


# file_name = "2020_보고서.xlsx"
# print(file_name.startswith('2020'))


# # Split() 이 문자를 공백 기준으로 나누고 배열로 저장
# a = "hello world"
# print(a.split())


# data = "039490     "
# data = data.rstrip()
# print(data)


# movie_rank = ['닥터 스트레인지', '스플릿', '럭키']

# movie_rank.append("배트맨")
# print(movie_rank)

# # insert(인덱스, 원소)
# movie_rank.insert(1, "슈퍼맨")
# print(movie_rank)

# del movie_rank[3]
# print(movie_rank)

# del movie_rank[2]
# del movie_rank[2]
# print(movie_rank)

# lang1 = ["C", "C++", "JAVA"]
# lang2 = ["Python", "Go", "C#"]

# print(lang1+lang2)

# cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
# print(len(cook))

# nums = [1, 2, 3, 4, 5]
# print(sum(nums)/len(nums))

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums[::2])

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums[1::2])

# nums = [1, 2, 3, 4, 5]
# print(nums[::-1])

# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print(" ".join(interest))
# print("\n".join(interest))

# string = "삼성전자/LG전자/Naver"
# print(string.split('/'))

# # 데이터 오름차순 정렬 (sort())
# data = [2, 4, 3, 1, 5, 10, 9]
# data.sort()
# print(data)

# data = [2, 4, 3, 1, 5, 10, 9]
# data2 = sorted(data)
# print(data2)

# my_variable = ()
# print(type(my_variable))

# movie_rank = (1, )
# print(type(movie_rank))

# # 튜플 정의는 꼭 가로가 없어도 된다
# t = 1, 2, 3, 4
# print(type(t))

# t = ('a', 'b', 'c')
# print(t)

# t = ('A', 'b', 'c')
# print(t)

# interest = ('삼성전자', 'LG전자', 'SK Hynix')
# print(list(interest))

# interest = ['삼성전자', 'LG전자', 'SK Hynix']
# print(tuple(interest))

# temp = ('apple', 'banana', 'cake')
# a, b, c = temp
# print(a, b, c)

# data = tuple(range(2, 100, 2))
# print(data)


# # # 튜플의 데이터 언패킹
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# _, *valid_score, _= scores
# print(valid_score)


# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}

# ice = list(icecream.keys())
# print(ice)
# print(sum(icecream.values()))

# # 딕셔너리가 있을 때 update 로 집어넣기
# new_product = {'팥빙수':2700, '아맛나':1000}
# icecream.update(new_product)

# print(icecream)


# keys = ("apple", "pear", "peach")
# vals = (300, 250, 400)
# print(dict(zip(keys, vals)))

# date = ['09/05', '09/06', '09/07', '09/08', '09/09']
# close_price = [10500, 10300, 10100, 10800, 11000]

# close_table = dict(zip(date, close_price))
# print(close_table)

# user = input("입력 : ")
# print(user*2)


# input_user = int(input("숫자 : "))

# if input_user - 20 < 0:
#     print(0)
# elif input_user - 20 > 255:
#     print(255)
# else:
#     print(input_user-20)


# input_user = input("시간 : ")
# print(input_user[-2:])

# if input_user[-2:] == "00":
#     print("정각")
# else:
#     print("정각 아님")


# fruit = ["사과", "포도", "홍시"]
# user = input("좋아하는 과일은?")

# if user in fruit:
#     print("정답")
# else:
#     print("오답")


# 119