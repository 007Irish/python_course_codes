def momos(n):
    def burger(hunk):
        def tikki(a):
            for i in range(n):
                hunk(a)
        return tikki
    return burger

@momos(18)
def say_hello(a):
    print(f"Hello! {a}")

say_hello("Irish")

'''
It replaces the function say_hello with this:
def burger(hunk):
    def tikki(a)
        for i in range(n)
            say_hello(a)
    return tikki
'''
        
    