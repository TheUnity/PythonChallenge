file = open('text.txt', 'r', encoding = 'utf-8')
newList = file.read().split()
newUpList = []
newFile = []

for i in newList:
    if len(i) > 6 and i[6] != ',' and i[6] != '.':
        newUpList.append(i.title())
    else:
        newUpList.append(i)
    newFile = str(' '.join(newUpList))

print(newFile)

with open('text.txt', 'w', encoding = 'utf-8') as file:
    file.write(newFile)