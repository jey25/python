import requests

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=700'
req_result = requests.get(url)
print(req_result.json())