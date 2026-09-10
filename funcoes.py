def dividir_seguro(a, b):
    """Divide 'a' por 'b', mas lança um erro tratado se b for 0."""
    if b == 0:
        raise ValueError("Não é possível dividir por zero")
    return a / b


def porcentagem(valor, percentual):
    """Calcula o percentual de um valor."""
    return valor * percentual / 100