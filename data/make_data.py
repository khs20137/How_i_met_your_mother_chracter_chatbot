# make_data.py
import re


script = open('How_I_Met_Your_Mother_S01_EP01.txt', 'r', encoding='utf-8')

speaking = []
for row in script.readlines():
    # print(row.strip())
    if len(row.strip().split(':')) >= 2:
        speaking.append(row.strip().split(':'))

for n in range(len(speaking)):
    if speaking[n][0] == 'Marshall':
        print(speaking[n-1])
        print(speaking[n])
        # print(speaking[n+1])

# 마셜을 먼저 만들어 보자 마셜과 다른 사람이 대화하는 것을 따로 빼오는 코드 생각해보기
