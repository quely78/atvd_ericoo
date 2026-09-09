def is_par(numero):
    """Retorna True se o número for par."""
    return numero % 2 == 0


def soma_lista(lista):
    """Retorna a soma de todos os elementos de uma lista."""
    return sum(lista)


def inverter_string(texto):
    """Retorna a string invertida."""
    return texto[::-1]


def maior_valor(lista):
    """Retorna o maior valor de uma lista. Lança ValueError se estiver vazia."""
    if not lista:
        raise ValueError("A lista não pode estar vazia.")
    return max(lista)


def eh_palindromo(texto):
    """Retorna True se o texto for palíndromo, ignorando espaços, pontuação e capitalização."""
    texto_normalizado = ''.join(
        caracter.lower() for caracter in texto if caracter.isalnum()
    )
    return texto_normalizado == texto_normalizado[::-1]
