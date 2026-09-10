import pytest
from funcoes import *


def test_dividir_seguro():
    resultado = dividir_seguro(10, 2)
    assert resultado == 5


def test_dividir_seguro_por_zero():
    with pytest.raises(ValueError):
        dividir_seguro(10, 0)


def test_porcentagem():
    resultado = porcentagem(200, 10)
    assert resultado == 20


def test_media_ponderada():
    resultado = media_ponderada([7, 8, 9], [2, 3, 5])
    assert resultado == pytest.approx(8.3)

def test_raiz_quadrada():
    resultado = raiz_quadrada(16)
    assert resultado == 4


def test_raiz_quadrada_negativo():
    with pytest.raises(ValueError):
        raiz_quadrada(-4)


def test_fatorial():
    resultado = fatorial(5)
    assert resultado == 120


def test_fatorial_zero():
    resultado = fatorial(0)
    assert resultado == 1


def test_fatorial_negativo():
    with pytest.raises(ValueError):
        fatorial(-3)
