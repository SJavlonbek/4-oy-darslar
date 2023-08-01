def son1(x):
    def son2(y):
        nonlocal x
        if len(x)>len(y):
            return sorted(x)
        else:
            return sorted(y)
    return son2

a=son1("Assalomu alaykum")
print(a("Hello world"))