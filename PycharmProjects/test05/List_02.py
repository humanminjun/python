#동시에 두개 이상의 리스트를 반복하기 위한 zip() 함수


questions = ['name', 'quest', 'color']
answers = ['song', 'hi', 'yellow']

for q, a in zip(questions, answers):
    print(f"what is your {q}? It is {a}")



