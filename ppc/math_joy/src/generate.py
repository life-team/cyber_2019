from random import choice, randint
flag = 'CTF{Joy_Math_from_txyza}'
math = '+-'
answer = {}
index = 0
for word in flag:
    answer[index] = ['X']
    current = ord(word)
    for i in range(50):
        zn = choice(math)
        b = randint(1, 1024)
        answer[index].append(zn)
        answer[index].append(str(b))
        current = current + b if zn == '+' else current - b
    answer[index].append('=')
    answer[index].append(str(current))
    index += 1
with open('enc.txt', 'w') as f:
    for key, value in answer.items():
        print(''.join(value))
        f.write(''.join(value) + '\n')
