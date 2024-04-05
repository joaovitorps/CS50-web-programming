def announce(f):
    def wrapper():
        print("The function is about to run")
        f()
        print("Done running the function")
    return wrapper

@announce
def hello():
    print("Hello world")

hello()
