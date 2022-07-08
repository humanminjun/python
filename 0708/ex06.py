# 슬라이스 응용
lst = [1, 2, 3, 4, 5, 6, 7, 8]
lst[0:3] = ['white', 'blue', 'red']
print(lst)

lst = [1, 2, 3, 4, 5, 6, 7, 8]
lst[::2] = [99, 99, 99, 99]
print(lst)

lst = [1, 2, 3, 4, 5, 6, 7, 8]
lst[:] = []
print(lst)

squares = [x * x for x in range(10)]
print("=>", squares)

squares = [x * x for x in range(10) if x %2 == 0]
print("=>", squares)