f = open('input.txt', 'r')
spec = f.read().split('\n')

def find_known_mapping(input):
    knownMapping = ['' for _ in range(7)]
    segHist = [0 for _ in range(7)]

    # find 0 segment (diff between number 1 and number 7 display)
    for entry in input[:2]:
        for ch in range(7):
            segHist[ch] += entry.count(chr(ord('a') + ch))
    knownMapping[0] = chr(ord('a') + segHist.index(1))

    # most other segments are unique because of how often they appear in the definition
    segHist = [0 for _ in range(7)]
    for entry in input:
        for ch in range(7):
            segHist[ch] += entry.count(chr(ord('a') + ch))
    knownMapping[1] = chr(ord('a') + segHist.index(6))
    knownMapping[2] = chr(ord('a') + segHist.index(8))
    if knownMapping[2] == knownMapping[0]:
        knownMapping[2] = chr(ord('a') + segHist.index(8, ord(knownMapping[2]) - ord('a') + 1))
    knownMapping[4] = chr(ord('a') + segHist.index(4))
    knownMapping[5] = chr(ord('a') + segHist.index(9))

    # differenciate seg 3 and seg 6 by number 4 display
    for seg in currInput[2]:
        if seg not in knownMapping:
            knownMapping[3] = seg
            knownMapping[6] = chr(ord('a') + segHist.index(7))
            if knownMapping[6] == knownMapping[3]:
                knownMapping[6] = chr(ord('a') + segHist.index(7, ord(knownMapping[3]) - ord('a') + 1))
    return knownMapping
def unique_2_number(unique):
    array = ['012456','25','02346','02356','1235','01356','013456','025','0123456','012356']
    return array.index(unique)

# setup
inputs = [0 for _ in range(len(spec))]
outputs = [0 for _ in range(len(spec))]
for index in range(len(spec)):
    line = spec[index].split('|')
    inputs[index] = line[0].split()
    inputs[index].sort(key=len)
    outputs[index] = line[1].split()

sum = 0
for index in range(len(inputs)):
    currInput = inputs[index]
    currOutput = outputs[index]
    knownMapping = find_known_mapping(currInput)

    number = ''
    for entry in currOutput:
        unique = ''
        for i in range(len(knownMapping)):
            if knownMapping[i] in entry:
                unique += str(i)
        number += str(unique_2_number(unique))
    sum += int(number)

print(sum)
