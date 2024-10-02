class Matriz:
    def __init__(self, valores: list):
        self.valores = valores

def mult_escalar(matrizA, numero):
    num_linhasA = len(matrizA.valores)
    resultado = []

    for i in range(num_linhasA):
        num_colA = len(matrizA.valores[i])
        linha = []
        for j in range(num_colA):
            linha.append(matrizA.valores[i][j] * numero)
        resultado.append(linha)

    matriz_resultado = Matriz(resultado)
    return matriz_resultado

matrizA = Matriz([[1, 2, 3], [4, 5, 6]])

resultado = mult_escalar(matrizA, 2)

print(resultado.valores)