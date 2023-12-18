num = int(input())
quocient = num
s = ''

while (quocient > 0):
    residu = quocient % 2
    s = str(residu) + s    
    quocient = quocient // 2
