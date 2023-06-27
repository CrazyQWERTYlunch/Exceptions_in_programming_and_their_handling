
def first_method(a,b):
    return a/b
def second_method(list1):
    for i in range(len(list1)+1):
        print(list1[i])
def third_method(a):
    return a + None

print(first_method(2,0)) # ZeroDivisionError: division by zero
print(second_method(list(map(int,input().split())))) # IndexError: list index out of range
print(third_method(5)) # TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
