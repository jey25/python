# import sys

# option = sys.argv[1]
# memo = sys.argv[2]

# if option == '-a':
#     memo = sys.argv[2]
#     f = open('memo.txt', 'a')
#     f.write(memo)
#     f.write('\n')
#     f.close()
# elif option == '-v':
#     f = open('memo.txt')
#     memo = f.read()
#     f.close()
#     print(memo)


# # PC 바탕화면에 메모장 생성하고 텍스트 입력
# f = open("C:/Users/eyjang/Desktop/매수종목1.txt", mode="wt", encoding="utf-8")
# f.write("005930 삼성전자\n")
# f.write("005380 현대차\n")
# f.write("035420 NAVER\n")
# f.close()


# # PC 바탕화면에 엑셀 파일 생성하고 텍스트 입력
# import csv

# f = open("C:/Users/eyjang/Desktop/매수종목.csv", mode="wt", encoding="cp949", newline='')
# writer = csv.writer(f)
# writer.writerow(["종목명", "종목코드", "PER"])
# writer.writerow(["삼성전자", "005930", 15.59])
# writer.writerow(["NAVER", "035420", 55.82])
# f.close()


# # 바탕화면의 파일을 읽어와 데이터를 리스트에 저장
# f = open("C:/Users/eyjang/Desktop/매수종목1.txt", encoding="utf-8")
# lines = f.readlines()   # python list

# codes = []
# for line in lines:
#     code = line.strip()  #'\n'
#     codes.append(code)

# print(codes)
# f.close()


# # 바탕화면의 파일을 읽어와 데이터를 딕셔너리에 저장
# f = open("C:/Users/eyjang/Desktop/매수종목1.txt", encoding="utf-8")
# lines = f.readlines()

# data = {}
# for line in lines:
#     line = line.strip()     # '\n' 제거
#     k, v = line.split()
#     #print(k, v)
#     data[k] = v

# print(data)
# f.close()

