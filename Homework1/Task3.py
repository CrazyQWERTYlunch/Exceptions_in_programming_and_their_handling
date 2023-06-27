

def create_arr(list1,list2):
    list3 = list()
    if len(list1) == len(list2):
        for i in range(len(list1)):
            if list2[i] == 0:
                raise RuntimeError("На ноль делить нельзя") # Аналог рантаймэксепшена java
            list3.append(list1[i]/list2[i])
    else:
        raise RuntimeError("Длина массивов не совпадает")
    return list3


ar1 = list(map(int,input("Введите через пробел значения элементов первого массива: ").split()))
ar2 = list(map(int,input("Введите через пробел значения элементов второго массива: ").split()))
print(*create_arr(ar1,ar2))

