with open('tmp.txt', 'r+') as f:
    for line in f:
        for i in line:
            if i == '\t':
                pass
                #print('tab')
            elif i == ' ':
                pass
                #print('space')

a = [[1,0],[0,0],[0,0]]
b = [[1,0],[1,0],[0,0]]
c = [[1,1],[0,0],[0,0]]
d = [[1,1],[0,1],[0,0]]

mylst = [a,b,c,d]

i1, i2, i3 = [],[],[]

for i in mylst:
    i1 += i[0]
    i2 += i[1]
    i3 += i[2]

print(i1, i2, i3)
