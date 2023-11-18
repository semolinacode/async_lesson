def foo(*args):
    print(args)
    print(len(args))


lst = ['Bob', 2, 3]
foo(*lst)
