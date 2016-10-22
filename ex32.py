num_list = [1,2,3,4,5,6,7,8]
string_list = []
random_list = [1,'sachin',5.78,'gupta']

for i in range(0,5):
    string_list.append(raw_input("enter element: "))

for number in num_list:
    print "%d"%number

for string in string_list:
    print string

for rn in random_list:
    print "%r"%rn