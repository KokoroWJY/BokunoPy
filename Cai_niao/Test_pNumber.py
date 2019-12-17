import re

line = "Cats are smarter than dogs"

"""" match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None """
matchObj = re.match('.* are .*', line, re.M | re.I)

# if matchObj:
#     print("matchObj.group() : ", matchObj.group())
#     print("matchObj.group(1) : ", matchObj.group(1))
#     print("matchObj.group(2) : ", matchObj.group(2))
# else:
#     print("No match!!")

if matchObj:
    print(matchObj.group())
else:
    print(matchObj)

""" search匹配整个字符串，直到找到一个匹配 """
matchObj = re.search('areg', line, re.M | re.I)

if matchObj:
    print(matchObj.group())
else:
    print(matchObj)