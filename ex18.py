def print_ar(*args):
    a1,a2 = args
    print "%s %s"%(a1,a2)

def print_ar2(a1,a2,a3):
    print "%s %s %s"%(a1,a2,a3)
    return a1,a2
#python can return multiple variables

print_ar('sachin','gupta')
ans1,ans2 = print_ar2('s','m','a')

print "%s %s"%(ans1,ans2)