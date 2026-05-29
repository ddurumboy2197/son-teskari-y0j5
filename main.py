def sonni_teskarilash(son):
    return int(str(son)[::-1])

son = int(input("Istalgan sonni kiriting: "))
print(sonni_teskarilash(son))
