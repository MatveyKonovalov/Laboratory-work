import random

n = random.randint(0, 10)
l = [[random.randint(1, 100), random.randint(1, 10)] for _ in range(n)]

print(f'test: {l}')
set_value_mas = set()
minn = 10 ** 100
maxx = -minn

for i in l:
    if i[0] > maxx:
        maxx = i[0]
    if i[0] < minn:
        minn = i[0]
sort_res = [[] for i in range(maxx - minn + 1)]

for i in l:
    ind_mas = i[0] - minn
    if i[0] in set_value_mas:
        vw = i[1] * sort_res[ind_mas][1]
        sort_res[ind_mas] = [i[0], vw]
    else:
        set_value_mas.add(i[0])
        sort_res[ind_mas] = i

print(f'result: {list(filter(lambda x: x, sort_res))}')
