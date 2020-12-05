# 2-3. boolean 자료형
print("ㅋ"*9)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))
print(not not not True)
print(not not not False)

# 2-4. 변수
animal = "강아지"
name = "사월이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "에요.")
hobby = "공놀이"
# 표준출력에서 쉼표는 문자형으로 변환할 필요가 없으며, 자동으로 공백(띄어쓰기)이 생성된다.
# 문자열 연결을 위해 쉼표와 '+'를 같이 사용할 수 있다.
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name, "는 ", age, "살이며, ", hobby + "을 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))

# 2-6. 퀴즈 #1
station = "사당" # + 신도림, 인천공항
print(station, "행 열차가 들어오고 있습니다.")

# 3-1. 연산자
print(2**3) # 2^3 = 8
print(10//3) # 3
print(3 == 4) # False
## and == &
print((3 > 0) and (3 < 5)) # True
print((3 > 0) & (3 < 5)) # True
## or == |
print((3 > 0) or (3 > 5)) # True
print((3 > 0) | (3 > 5)) # True
print(4 < 5 < 7) # True
print(4 > 5 < 7) # False

# 3-3. 숫자처리함수
print(abs(-5)) # 절댓값, 5
print(pow(4, 2)) # 제곱, 4^2 = 16
print(max(5, 12)) # 최댓값, 12
print(min(5, 12)) # 최솟값, 5
print(round(3.14)) # 반올림, 3

from math import *
print(floor(4.99)) # 내림, 4
print(ceil(3.14)) # 올림, 4
print(sqrt(16)) # 제곱근, 4

# 3-4. 랜덤함수
from random import *
print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 `이하`
print(int(random() * 10)) # 0 ~ 10
print(int(random() * 10) + 1) # 1 ~ 10 
print(int(random() * 45) + 1) # 1 ~ 45
print(randrange(1, 46)) # 1 ~ 46 `미만`
print(randint(1, 45)) # 1 ~ 45 `이하`

# 3-5. 퀴즈 #2
date = int(random() * 28 + 4)
date = randrange(4, 29)
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "일로 선정되었습니다.")

# push test