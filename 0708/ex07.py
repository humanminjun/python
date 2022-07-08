#튜플 / 딕셔너리 / 세트

#튜플 - 변경불가
fruits = ("apple", "banana", "grape")
print(fruits)
print(fruits[0])
for f in fruits:
    print(f, end=" ")

#튜플을 리스트로
myTuple = (1, 2, 3, 4)
myList = list(myTuple)
print()
print(myList)

#딕셔너리 - key/value -{}
#ex08로

#set - 중복불가 - {}
numbers = {1, 2, 3}
print("set=", numbers)

numbers = set([1, 2, 3, 4, 5]) #중복을 허락하지 않음
print("set=", numbers)

#set함수 연산
aList = [1, 2, 3, 4, 5, 1, 2]
result = {x for x in aList if x % 2 == 0}
print("x=%2", result)

#set - 교집합 / 합집합 / 차집합
A = {"apple", "banana", "grape"}
B = {"apple", "banana", "kiwi"}
C = A | B
D = A & B
E = A - B
print("합집합", C)
print("교집합", D)
print("차집합", E)