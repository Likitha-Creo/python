def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)
    
standard_arg(1)
standard_arg(arg = 2)
pos_only_arg(3)
kwd_only_arg(arg = 4)
combined_example(5, 6, kwd_only = 7)
combined_example(8, standard = 9, kwd_only = 10)
combined_example(pos_only = 11, standard = 12, kwd_only = 13)
combined_example(14, 15, 16)
