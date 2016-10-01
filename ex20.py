from sys import argv

script,filename = argv

def print_all(f):
    print f.read()


def print_a_line(line_no,f):
    print line_no,f.readline()


def rewind(f):
    f.seek(0)


file = open(filename)

print_all(file)

rewind(file)

print_a_line(1,file)
print_a_line(2,file)
print_a_line(3,file)

