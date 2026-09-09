import pytest

from funcoes import (
    eh_palindromo,
    inverter_string,
    is_par,
    maior_valor,
    soma_lista,
)


@pytest.mark.parametrize(
    "numero, esperado",
    [
        (2, True),
        (5, False),
        (0, True),
        (-4, True),
    ],
)
def test_is_par(numero, esperado):
    assert is_par(numero) is esperado


@pytest.mark.parametrize(
    "lista, esperado",
    [
        ([1, 2, 3, 4], 10),
        ([], 0),
        ([10, -2, 3], 11),
    ],
)
def test_soma_lista(lista, esperado):
    assert soma_lista(lista) == esperado


@pytest.mark.parametrize(
    "texto, esperado",
    [
        ("python", "nohtyp"),
        ("", ""),
        ("abc123", "321cba"),
    ],
)
def test_inverter_string(texto, esperado):
    assert inverter_string(texto) == esperado


@pytest.mark.parametrize(
    "lista, esperado",
    [
        ([3, 1, 9, 4], 9),
        ([10], 10),
        ([-5, -2, -9], -2),
    ],
)
def test_maior_valor(lista, esperado):
    assert maior_valor(lista) == esperado


def test_maior_valor_lista_vazia():
    with pytest.raises(ValueError, match="A lista não pode estar vazia"):
        maior_valor([])


@pytest.mark.parametrize(
    "texto, esperado",
    [
        ("arara", True),
        ("A man, a plan, a canal: Panama", True),
        ("python", False),
        ("  a   " , True),
    ],
)
def test_eh_palindromo(texto, esperado):
    assert eh_palindromo(texto) is esperado
