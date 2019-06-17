from text  import blindmanObject
blindman = blindmanObject()
def decipher(file):
    bins = []
    cipheredFile = open(file, 'r+')

    for line in cipheredFile:
        for i in line:
            if i == '\t':
                bins.append(1)
            elif i == ' ':
                bins.append(0)

    refinedbins = [ bins[i:i+2] for i in range(0, len(bins), 2) ]
    refinedbins = [ refinedbins[i:i+len(refinedbins)//3] for i in range(0, len(refinedbins),len(refinedbins)//3 )]

    r1, r2,r3 = refinedbins
    plaintext = ""

    for i in range(0, len(r1)):
        letterCode = [r1[i]] + [r2[i]] + [r3[i]]
        for key, value in blindman.items():
            if value ==  letterCode:
                plaintext += key

    return plaintext
