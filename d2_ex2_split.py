def do_line(line):
    words = line.split("임금")
    #words = line.split()
    if len(words) > 0: print(len(words[0]), words[0])
    for word in words:
        print(word)

def do_file(name):
    with open(name, 'r') as f: lines = f.readlines()
    for line in lines: do_line(line)


do_file("salary.txt")
