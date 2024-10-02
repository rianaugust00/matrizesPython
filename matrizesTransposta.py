class Matriz:
    def __init__(self, valores: list):
        self.valores = valores

    def transposta(self):
        # Obter o número de linhas e colunas
        num_linhasA = len(self.valores)
        num_colA = len(self.valores[0])

        # Criar uma lista vazia para a matriz transposta
        resultado = []

        # Loop sobre as colunas da matriz original
        for j in range(num_colA):
            linha = []
            # Loop sobre as linhas da matriz original
            for i in range(num_linhasA):
                linha.append(self.valores[i][j])
            resultado.append(linha)

        # Criar uma nova instância de Matriz para o resultado transposto
        matriz_resultado = Matriz(resultado)
        return matriz_resultado

# Exemplo de uso
matrizA = Matriz([[1, 2, 3], [4, 5, 6]])
matriz_transposta = matrizA.transposta()

print(matriz_transposta.valores)
