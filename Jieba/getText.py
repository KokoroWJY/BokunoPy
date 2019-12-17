import jieba

# 给Hamet(英文版 哈姆雷特)分词
def getText():
    txt = open("Hamet.txt", 'r').read()
    txt = txt.lower() # 所有字母变为小写 避免大小写的影响
    for ch in 'i"#$%&()+,-/;:<=>?[]@^"*\|~`' + "'":
        txt = txt.replace(ch, ' ')
    return txt

hamletTxt = getText()
worlds = hamletTxt.split()
counts = {}

# 遍历列表 使其形成字典
for world in worlds:
    # counts[world] 检查world这个键
    counts[world] = counts.get(world, 0) + 1