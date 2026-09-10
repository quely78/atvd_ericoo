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