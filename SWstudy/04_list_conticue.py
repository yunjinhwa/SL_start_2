'''
    continue
'''

#리스트의 값 10개 중에서 10보다 큰 수를 출력하시오

import random

numbers = []
for i in range(10):
    numbers.append(random.randint(1,99))

print('생성된 리스트',numbers)

print()
print('-'*65)
print()

print('리스트 값 중 10보다 큰 수 - 반복문 사용')

for i in numbers:
    if i >= 10:
        print(i,end=', ')

print()
print()
print('-'*65)
print()

print('리스트 값 중 10보다 큰 수 -continue 사용')
for i in numbers:
    if i < 10:
        continue
    print(i,end=', ')

print()
print('-'*65)
print()

#1~~30 사이의 수 중에서 7의 배수만 출력하시오. - continue 사용

print("1~30 사이 중 7의 배수 출력")

num7 = (range(1,30))
for i in num7:
    if i % 7 != 0:
        continue
    print(i,end=', ')
print()



