def custom_max(x,y):
    if x < y:
        return print(f"El numero mayor es {y}")
    else:
        return print(f"El numero mayor es {x}")
    
custom_max(int(input("primer Valor ")), int(input(" Segundo Valor ")))