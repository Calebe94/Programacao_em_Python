def do_some_thing(*args):
    arg1,arg2 = args
    print("arg1:%r,arg2:%r"%(arg1,arg2))
def print_some(*args):
    arg1,arg2 = args
    print("%s %s"%(arg1,arg2))
do_some_thing("Loko","É Poko")
print_some("LOKO","É POKO")
