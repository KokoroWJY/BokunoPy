# 给Hamet(英文版 哈姆雷特)分词

def getText():
    """全文变为小写并将特殊符号变为空格 以空格分割"""
    txt = open("Hamet.txt", 'r').read()
    txt = txt.lower()  # 所有字母变为小写 避免大小写的影响
    for ch in '!"#$%&()+,-/;:<=>?[]@^"*\|~`' + "'":
        txt = txt.replace(ch, " ")
    return txt


hamletTxt = getText()
worlds = hamletTxt.split()
counts = {}

# 遍历列表 使其形成字典
for world in worlds:
    # counts[world] 检查world这个键
    counts[world] = counts.get(world, 0) + 1

items = list(counts.items())
""" lambda 用来指定列表中使用那一个多元选择的列作为排序列 默认:从小到大
reverse=True 返回顺序从大到小"""
items.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    world, counts = items[i]
    print("{0:<10}{1:>5}".format(world, counts))
