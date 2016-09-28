from sys import argv

script,filename = argv

file = open(filename,'w+')

#print "contents of file : "
#print text.read()
print "truncating the file!\nhit ^c to stop.\n" \
      "hit return to continue"

raw_input("?")

print "truncating the file"
file.truncate()

print "enter new data to enter into file"
line1 = raw_input()
line2 = raw_input()
line3 = raw_input()

file.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

#file = open(filename)
print "new contents of file are : ",file.read()

file.close()