from text import blindmanObject
blindman = blindmanObject()

def cipher(msg):

    i0, i1, i2 = [],[],[]

    for i in msg:
        i0 += blindman[i][0]
        i1 += blindman[i][1]
        i2 += blindman[i][2]
    cipher = [i0, i1, i2]

    newFile = open('ciphered.txt', 'w')

    for i in cipher:
        for j in i:
            if j == 1:
                newFile.write('\t')
            elif j == 0:
                newFile.write(' ')
        newFile.write('\n')
