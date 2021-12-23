# make_data.py
import re
import collections
import pprint


def get_data(path):
    script = open(path, 'r', encoding='utf-8')

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

    characters = list(set(characters))

    return characters, data


# 대본은 가져온 후 인물별로 말을 나눠 담는 코드
    # Marshall, Ranjit, Barney, Lily, Robin, Ted, Narrator, Yasmine = \
    #     [], [], [], [], [], [], [], []
    # for row in data:
    #     if row[0] == 'Marshall':
    #         Marshall.append(row[1])
    #     if row[0] == 'Ranjit':
    #         Ranjit.append(row[1])
    #     if row[0] == 'Barney':
    #         Barney.append(row[1])
    #     if row[0] == 'Lily':
    #         Lily.append(row[1])
    #     if row[0] == 'Robin':
    #         Robin.append(row[1])
    #     if row[0] == 'Ted':
    #         Ted.append(row[1])
    #     if row[0] == 'Narrator':
    #         Narrator.append(row[1])
    #     if row[0] == 'Yasmine':
    #         Yasmine.append(row[1])

characters, data_hall = [], []
for num in range(1, 23):
    num = '0' + str(num) if len(str(num)) < 2 else str(num)
    character, data = get_data(f'How_I_Met_Your_Mother_S01_EP%s.txt' % num)
    characters.append(character)
    data_hall.append(data)

pprint.pprint(characters)
pprint.pprint(data_hall)
