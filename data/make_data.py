# make_data.py
import re
import collections


script = open('How_I_Met_Your_Mother_S01_EP01.txt', 'r', encoding='utf-8')

speaking = []
for row in script.readlines():
    # print(row.strip())
    if len(row.strip().split(':')) >= 2:
        speaking.append(row.strip().split(':'))

characters, data = [], []
for n in range(len(speaking)):
    if speaking[n][0] == 'Marshall':
        # print(speaking[n-1])
        # print(speaking[n])
        characters.append(speaking[n-1][0])
        data.append(speaking[n-1])
        characters.append(speaking[n][0])
        data.append(speaking[n])

print(characters)
print(collections.Counter(characters))
characters = list(set(characters))
# 'Marshall', 'Ranjit', 'Barney', 'Lily', 'Robin', 'Ted', 'Narrator', 'Yasmine'

Marshall, Ranjit, Barney, Lily, Robin, Ted, Narrator, Yasmine = \
    [], [], [], [], [], [], [], []
for row in data:
    if row[0] == 'Marshall':
        Marshall.append(row[1])
    if row[0] == 'Ranjit':
        Ranjit.append(row[1])
    if row[0] == 'Barney':
        Barney.append(row[1])
    if row[0] == 'Lily':
        Lily.append(row[1])
    if row[0] == 'Robin':
        Robin.append(row[1])
    if row[0] == 'Ted':
        Ted.append(row[1])
    if row[0] == 'Narrator':
        Narrator.append(row[1])
    if row[0] == 'Yasmine':
        Yasmine.append(row[1])


# 마셜을 먼저 만들어 보자 마셜과 다른 사람이 대화하는 것을 따로 빼오는 코드 생각해보기
