def outer_fun():
    a = 20
    def inner_fun():
        a = 30
        print(a)
    inner_fun()
    print(a)
a = 10
outer_fun()
print(a)
