# 리스트의 탐색과 삭제

#탐색
heroes = ["아이언맨", "토르", "헐크", "블랙위도우", "토르"]
n = heroes.index("헐크")
print(n)

n = heroes.index("토르")
print(n)

#삭제
heroes = ["아이언맨", "토르", "헐크"]
h = heroes.pop(1) #인덱스
print(heroes)

heroes = ["아이언맨", "토르", "헐크"]
h = heroes.remove("토르") #데이터
print(heroes)

