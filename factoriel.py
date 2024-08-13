def factoriel(num):
    if num == 0:
        return 1 
    else:
        return num * factoriel(num - 1)

print(factoriel(6))