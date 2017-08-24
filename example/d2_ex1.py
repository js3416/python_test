f = open('data', 'r')
#read_data = f.read()
#lines = f.readlines()
i=0
for i in range(0,10):
    line = f.readline()
    if i != int(line):
        print('i=',int(line))

