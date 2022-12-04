f = open('input.txt', 'r')
lines = f.read().split('\n')

def getCommonBit(list, index):
    bitHist = 0
    for line in list:
        if line[index] == '0':
            bitHist -= 1
        else:
            bitHist += 1

    if bitHist < 0:
        return '0'
    else:
        return '1'

oxygenList = [i for i in lines]
co2List = [i for i in lines]
for index in range(len(lines[0])):
    oxygenBit = getCommonBit(oxygenList, index)
    co2Bit = getCommonBit(co2List, index)
    
    for line in lines:
        if len(oxygenList) > 1 and line in oxygenList and line[index] != oxygenBit:
            oxygenList.remove(line)
        if len(co2List) > 1 and line in co2List and line[index] == co2Bit:
            co2List.remove(line)
    
oxygen = int(oxygenList[0], 2)
co2 = int(co2List[0], 2)
print(oxygen * co2)
