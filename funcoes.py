def dividir_seguro(a, b):
    """Divide 'a' por 'b', mas lança um erro tratado se b for 0."""
    if b == 0:
        raise ValueError("Não é possível dividir por zero")
    return a / b


def porcentagem(valor, percentual):
    """Calcula o percentual de um valor."""
    return valor * percentual / 100


def media_ponderada(notas, pesos):
    """Calcula a média ponderada de uma lista de notas e pesos."""
    if len(notas) != len(pesos):
        raise ValueError("Notas e pesos devem ter o mesmo tamanho")

    if not notas or not pesos:
        raise ValueError("Notas e pesos não podem estar vazios")

    soma_pesos = sum(pesos)
    if soma_pesos == 0:
        raise ValueError("A soma dos pesos deve ser diferente de zero")

    return sum(nota * peso for nota, peso in zip(notas, pesos)) / soma_pesos


def raiz_quadrada(numero):
    """Calcula a raiz quadrada de um número, lançando erro se for negativo."""
    if numero < 0:
        raise ValueError("Não é possível calcular raiz quadrada de número negativo")
    return numero ** 0.5

def fatorial(numero):
    """Calcula o fatorial de um número inteiro não negativo."""
    if numero < 0:
        raise ValueError("Não é possível calcular fatorial de número negativo")
    resultado = 1
    for i in range(2, numero + 1):
        resultado *= i
    return resultado
