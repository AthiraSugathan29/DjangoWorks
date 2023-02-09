def smart_dec(fn):
    def wrapper(n1,n2):
        if n1 < n2:
            n1,n2 = n2,n1
            return fn(n1,n2)
    return wrapper

@smart_dec
def sub(n1, n2):
    # if n1 < n2:
    #     n1,n2 = n2,n1
    return n1 - n2

@smart_dec
def div(n1, n2):
    # if n1 < n2:
    #     n1,n2 = n2,n1
    return n1 / n2


print(sub(5, 10))
print(div(5, 10))
