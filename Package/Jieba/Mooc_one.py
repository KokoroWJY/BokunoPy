import jieba

# mooc jieba的基本语法测试

text = "中华人民共和国是伟大的"
print(text)
print("精确模式: ")
print(jieba.lcut(text))
print("精确模式的全模式: ")
print(jieba.lcut(text, cut_all=True))
print()
print("搜索引擎模式: ")
print(jieba.lcut_for_search(text))
