# 변수 - 타입이 없음(할당하면 타입잉 생김)
# str, int, float, bool

# 문자형 - "", ''
from ntpath import join


str1 = "Life is too short, You need Python"
str2 = 'Life is too short, You need Python'
str3 = """
Life is too short, You need Python
"""
str4 = '''
Life is too short, You need Python
'''
str5="Python's favorite food"

print(str1)
print(str2)
print(str3)
print(str4)
# Enter 도 문자열로 인식
print(str5)

# + : 문자열 연결
head = "Python"
tail = "is fun"
print(head+tail)

# * : 반복
a = "Python"
print(a * 2)

print("*"*50)
print("My Program")
print("*"*50)

# 문자열 인덱싱
str1 = "Life is too short"
# 왼쪽을 기준으로 0
print("str1[3]", str1[3])   #e
# 오른쪽을 기준으로 -1
print("str1[-3]", str1[-3]) #o
print()
# 마지막  숫자 범위는 포함 안함
# 범위 지정
print("str1[0:4]", str1[0:4])
print("str1[4:8]", str1[4:8])
print("str1[9:]", str1[9:])
print("str1[:17]", str1[:17])
print("str1[0:-4]", str1[0:-4])

# 싨습
str2 = "20220520Sunny"
# date 변수에 날짜만 담기
date = str2[0:8]

# weather 변수에 날씨만 담기
weather = str2[8:]

# date 변수에 있는 값을 2022-05-20 출력
year = date[0:4]
month = date[4:6]
day = date[6:]
print(year, month, day, sep="-")

# date, weather 출력 2022-05-20 Sunny 출력
print(year, month, day, sep="-",end=" ")
print(weather)

# 문자열 관련 함수들
# len()
print("문자열 길이", len(str1))
# count()
print("문자열에 포함된 특정 문자의 수", str1.count('t'))
print("문자열에 포함된 특정 문자의 수 : %d" % str1.count('t'))
print("문자열에 포함된 특정 문자의 수 : {}".format(str1.count('t')))
# find('찾을 문자', '시작 위치')
print("특정 문자가 시작되는 첫번째 위치 반환", str1.find('i'))
print("특정 문자가 시작되는 첫번째 위치 반환", str1.find('k'))
print("특정 문자가 시작되는 첫번째 위치 반환", str1.find('i', 4))
# 4번째 이후부터 찾도록 지정(시작 위치 지정 가능)(옵션)(안줘도 상관X)
# index()
print("특정 문자가 시작되는 첫번째 위치 반환", str1.index('i'))
# print("특정 문자가 시작되는 첫번째 위치 반환", str1.index('k'))     # ValueError: substring not found
# find() 와 index()의 역할은 동일.
# 차이점 : 없는 문자를 찾을 때 error 발생 여부
# index() : 찾는 문자열이 없다면 error 발생
# find() : 찾는 문자열이 없어도 error 발생X
print()
# startswith(), endswith()
print(str1.startswith("L")) # True
print(str1.startswith("l")) # False
# bool 타입으로 리턴. 대소문자 구분
print(str1.endswith("t")) # True
print(str1.endswith("T")) # False
print()
# join() : 삽입
a = ","
print(a.join("abcde"))
# abcde 라는 문자열 사이에 a(,) 삽입
print()
# upper / lower : 대소문자 변경
a = "abcde"
print("소문자를 대문자로 변경", a.upper())
a = "ABCDE"
print("대문자를 소문자로 변경", a.lower())
# swapcase() : 대소문자를 상호 변환
a = "Python is Easy"
print(a.swapcase())
# title() : 첫글자만 대문자
print("python Is Easy".title())

print("abc" == "ABC")   # False

print()

# 공백 제거 : strip(), lstrip(), rstrip()
a = "   hi   "
print(a.lstrip())   # 왼쪽 공백 제거
print(a.strip())    # 양쪽 공백 제거
print(a.rstrip())   # 오른쪽 공백 제거
print()
# replace() : 문자열 바꾸기
print(str1.replace("Life", "Your leg"))
print()
# split() : 문자열 나누기(default : 공백)
print(str1.split()) # ['Life', 'is', 'too', 'short']    리스트 구조로 리턴됨 list[str]
a = "a:b:c:d"
print(a.split(":")) # ['a', 'b', 'c', 'd']
# splitlines() : 줄바꿈을 기준으로 나누기
a = "하나\n둘\n셋"
print(a.splitlines())   # ['하나', '둘', '셋']

# 문자열 구성 파악
print("1234".isdigit())
print('abcd'.isalpha())
print('abc123'.isalnum())
print('abcd'.islower())
print("ABCD".isupper())

# 실습 : 암호 생성
# http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 . 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 e 문자 개수 + ! 로 구성 => nav51!
# 결과 : nav51!
url = "http://naver.com"
url = url.replace("httpL//","")
url = url[:url.find(".")]
print(url)
e_cnt = url.count("e")

# 문자 + 숫자 : 연결되지 않음(에러 발생)
# 문자 + str(숫자) : 연결
password = url[:3] + str(len(url)) + str(e_cnt) + "!" # TypeError: can only concatenate str (not "int") to str
print(password)

