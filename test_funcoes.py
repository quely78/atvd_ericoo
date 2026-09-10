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