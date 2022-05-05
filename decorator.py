from traceback import print_tb


def dec(func):
    def wrap():
        print("before")
        func()
        print("after")
    return wrap

# новый синтасис
@dec()
def foo():
    print("hello!")

# старый синтаксис
# foo = dec(foo)
foo()