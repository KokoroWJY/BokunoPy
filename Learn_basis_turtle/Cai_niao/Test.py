a = input()
b = str(a)
printOut = ''

def getNum(Number):
    if Number == '0':
        return '零'
    elif Number == '1':
        return '一'
    elif Number == '2':
        return "二"
    elif Number == '3':
        return '三'
    elif Number == '4':
        return '四'
    elif Number == '5':
        return '五'
    elif Number == '6':
        return '六'
    elif Number == '7':
        return '七'
    elif Number == '8':
        return '八'
    elif Number == '9':
        return '九'

for i in range(len(b)):
    printOut = printOut + getNum(a[i])
print(printOut)