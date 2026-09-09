import pytest
from funcoes import *


def test_dividir_seguro():
    resultado = dividir_seguro(10, 2)
    assert resultado == 5


def test_dividir_seguro_por_zero():
    with pytest.raises(ValueError):
        dividir_seguro(10, 0)