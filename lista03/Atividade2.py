def repetir(x):
    for i in range(1, x+1):
        aux = ''
        for j in range(0, i):
            aux+=str(j+1) + '\t'
        print(f"{aux}")
num=int(input("Insira qual número de vezes deseja repetir o processo: "))
repetir(num)