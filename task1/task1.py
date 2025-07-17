import sys

n = int(sys.argv[1])
m = int(sys.argv[2])

path = ''
array = ''.join([str(i) for i in range(1, n+1)])
piece = array + ''

o = 0
l = m * 1

while True:
    if len(array[o:l]) < m:
        array += array
    piece = array[o:l]
    path += piece[0]
    if piece[-1] == array[0]:
        break
    else:
        o += m - 1
        l += m - 1

print(path)
