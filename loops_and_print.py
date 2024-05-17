def enumerate_list(list):
    resultado= []
    indice = 0
    for i in list:
        if i: 
            resultado.append(f"{indice}. {i}")
            indice += 1
    return resultado
def enumerate_backwards(list):
    resultado = []
    indice = 0
    for i in list:
        if i:  
            inversa = i[::-1]
            resultado.append(f"{indice}. {inversa}")
            indice += 1
    return resultado
colores = ["Red", "Green", "", "White", "Black"]
