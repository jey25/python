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


