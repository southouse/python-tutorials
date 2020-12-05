print("ㅋ"*9)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))
print(not not not True)
print(not not not False)

# 애완동물을 소개해 주세요~
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
print(name, "는 ", age, "살이며, ", hobby + "을 아주 좋아해요")ㅇ
print(name + "는 어른일까요? " + str(is_adult))

station = "사당" # + 신도림, 인천공항
print(station, "행 열차가 들어오고 있습니다.")

