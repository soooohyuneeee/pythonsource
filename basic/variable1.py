# 변수 - 타입이 없음 (할당하면 타입이 생김)
# 자바스크립트랑 같은 개념(?)
# str, int, float, bool

# 숫자형 - 정수, 실수, 8진수, 16진수 ...
a = 13
a = -7
a =  0
a = 1.2
a = 0o177   # 8진수 (0o로 시작)
a = 0x8fff  # 16진수 (0x로 시작)

# 사칙연산
# a = 3
# b = 4
a, b = 3, 4 #(앞에서 부터 순서대로 대입. a = 3, b = 4)
print(a + b)    # 7
print(a / b)    # 0.75  (정수 나눗셈이 아님. 실수개념. 소숫점 붙으면 다 보여줌)
print(a // b)   # 0 (정수 나눗셈)
print(a % b)    # 3 (나머지 값)
print(a ** b)   # 81 (제곱)


