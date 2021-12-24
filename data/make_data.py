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
            characters.append(re.sub('(\(.+?\))', '', speaking[n-1][0]).strip())
            data.append([re.sub('(\(.+?\))', '', speaking[n-1][0]).strip(), speaking[n-1][1]])
            characters.append(re.sub('(\(.+?\))', '', speaking[n][0]).strip())
            data.append([re.sub('(\(.+?\))', '', speaking[n][0]).strip(), speaking[n][1]])

    characters = list(set(characters))

    return characters, data


def none_use(data):
    data = re.sub('', '', data)
    return data


characters, data_hall = [], []
for num in range(1, 23):
    num = '0' + str(num) if len(str(num)) < 2 else str(num)
    character, data = get_data(f'How_I_Met_Your_Mother_S01_EP%s.txt' % num)
    characters.append(character)
    data_hall.append(data)

# pprint.pprint(characters)
# pprint.pprint(data_hall)

characters = set([name for names in characters for name in names])

data_dict = {}
for name in characters:
    data_dict[name] = []

for episode in data_hall:
    for k, v in episode:
        data_dict[k].append(v)

print(data_dict)

# none_use()

# 시즌 1 캐릭터별 데이터 딕셔너리로 저장 까지.
