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
            if speaking[n-1][0] != 'Marshall':
                characters.append(re.sub('(\(.+?\))', '', speaking[n-1][0]).strip())
                data.append([re.sub('(\(.+?\))', '', speaking[n-1][0]).strip(), speaking[n-1][1]])
            characters.append(re.sub('(\(.+?\))', '', speaking[n][0]).strip())
            data.append([re.sub('(\(.+?\))', '', speaking[n][0]).strip(), speaking[n][1]])

    characters = list(set(characters))

    return characters, data


def make_unique(data):
    rows = ''
    for name in data:
        for row in data[name]:
            rows += ' ' + row

    rows = rows.split()

    # print(len(rows))                # 17475
    # print(len(set(rows)))           # 2781

    return set(rows)


def clean_str(rows):
    rows = re.sub('(\(.+?\))', '', rows)
    rows = re.sub('[\,\.\?\!\"\…\“\”\*]', '', rows)
    rows = re.sub('-', ' ', rows)
    rows = re.sub('—', ' ', rows)
    rows = re.sub('’', '\'', rows)

    return rows.lower().strip()


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
        v = clean_str(v)
        data_dict[k].append(v)

rows = make_unique(data_dict)
rows = sorted(list(rows))
# print(len(sorted(rows)))        # 2781

idx2vocab, vocab2idx = {}, {}
for i, row in enumerate(rows, 1):
    idx2vocab[i] = row
    vocab2idx[row] = i

# print(idx2vocab)
# print(vocab2idx)

# exit()

for i in data_hall:
    for j in i:
        speech = clean_str(j[1])
        # print(speech)
        print(j[0], speech)
        print(j[0], [vocab2idx[word] for word in speech.split()])

# 보캅 만듬
