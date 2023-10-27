import pytest
from src.ej2_7 import renta

@pytest.mark.parametrize(
"renta_anual , expected",
[
    (34000 , "Tipo impositivo del 20%"),
    (78000 , "Tipo impositivo del 45%"),
    (12345 , "Tipo impositivo del 15%"), 
     (256 , "Tipo impositivo del 5%"),
    (43211 , "Tipo impositivo del 30%")
])
def test_grupos(renta_anual , expected):
    assert renta(renta_anual) == expected