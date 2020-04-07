""" 贪婪算法 """

# test
# arr = [1, 2, 2, 3, 3, 3, 3]
# print(set(arr))

""" 你办了个广播节目, 要让所有地方的听众都收听到 """
states_needed = {"mt", "wa", "or", 'id', 'nv', 'ut', 'az'}  # 集合 需要覆盖的地方

# 广播台清单
stations = {}
stations['kone'] = set(["id", "nv", "ut"])
stations['ktwo'] = {'wa', 'id', 'mt'}
stations['kthree'] = {'or', 'nv', 'ca'}
stations['kfour'] = {'nv', 'ut'}
stations['kfive'] = set(['ca', 'az'])

final_stations = set()  # 储存最终的选择

while states_needed:
    best_station = None  # 存储覆盖了最多的广播台
    states_covered = set()  # 存储该广播台覆盖的所有未覆盖的地方
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station  # & 交集, | 并集, - 差集
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)
