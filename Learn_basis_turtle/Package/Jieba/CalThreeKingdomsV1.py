import jieba

txt = open("三国演义.txt", "r", encoding="utf-8").read()
# 非人名的集合
excludes = {"将军", "却说", "荆州", "二人", "不可", "不能", "如此", "左右", "商议",
            "次日", "军士", "如何", "军士", "军马", "引兵", "大喜", "天下", "东吴",
            "于是", "今日", "不敢", "魏兵"}  # 不全 个人懒得写了...
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "诸葛亮" or word == "孔明曰":
        rword = "孔明"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    elif word == '玄德' or word == '玄德曰':
        rword = "刘备"
    elif word == '孟德' or word == '孟德曰':
        rword = '曹操'
    else:
        rword = word
        counts[rword] = counts.get(word, 0) + 1
# 删除非人名的
for word in excludes:
    del counts[word]
# 列表排序
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(15):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
