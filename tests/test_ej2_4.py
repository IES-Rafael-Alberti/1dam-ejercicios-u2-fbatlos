import pytest
from src.ej2_4 import par_o_impar

@pytest.mark.parametrize(
"numero , expected",
[
    (21 , "Tu numero es impar"),
    (11 , "Tu numero es impar"),
    (50 , "Tu numero es par"),
    (200, "Tu numero es par"), 
    (63 , "Tu numero es impar")
])
def test_par_o_impar(numero , expected):
    assert par_o_impar(numero) == expected