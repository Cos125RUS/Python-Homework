with open('RLE.txt','r') as file:
    rle = dict(map(lambda f: f.split(), (line.replace('\n','') for line in file)))
with open('Unpacked.txt', 'w') as file:
    for i in rle.keys():
        file.write(chr(int(i)) * int(rle[i]))
