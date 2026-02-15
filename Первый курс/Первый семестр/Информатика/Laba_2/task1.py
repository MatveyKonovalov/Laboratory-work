def search(s, users):
    res = []
    for user in users:
        for key in user:
            if s.lower() in user[key].lower():
                res.append(user)
                break
        else:
            fio = user['last_name'] + ' ' + user['first_name'] + ' ' + user['second_name']
            if s.lower() in fio.lower():
                res.append(user)
            else:
                fio = user['last_name'] + ' '
                for i in ['first_name', 'second_name']:
                    if not user[i]:
                        continue
                    fio += user[i][0]
                    fio += ' '
                if s.replace('.', ' ').lower().strip() in fio.lower().strip():
                    res.append(user)
    return res


def create_sp(s):
    res = []
    data_keys = {'first_name', 'second_name', 'last_name', 'phone', 'email'}
    users = ''.join(map(lambda x: chr(int(x)), s.split('#'))).split(';')
    for user in users:
        par = user.split(',')
        us = {}
        for p in par:
            key, val = p.split('=')
            if key in data_keys:
                us[key] = str(val)
        ###
        for key in data_keys:
            if key not in us:
                us[key] = ''
        ###
        res.append(us.copy())
    return res


with open('test1.txt') as file:
    data = ''
    for i in file.readlines():
        data += i.strip()
mas = create_sp(data)
pattern = ["lipa", "Collaton", "Collaton Felipa", "collaton Felipa W",
           "2@yahoo", "337", "Collaton F.W", "Felipa"]
for i in pattern:
    ans = search(i, mas)
    print(ans)
