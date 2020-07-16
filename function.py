
def greet(name):
    print('Good morning, ' + name)


greet('Priyesh Kumar')


def outer():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x)

    inner()
    print(x)


outer()
