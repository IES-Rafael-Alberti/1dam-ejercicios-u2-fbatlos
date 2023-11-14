import pytest
from src.ej2_3 import disvision

@pytest.mark.parametrize(
"dividendo , divisor , expected",
[
    (20 , 2 , 10),
    (10 , 0 , "ERROR"),
    (5 , 2 , 2.5),
    (300, 3 , 100), 
    (63 , 7 , 9)
])
def test_contraseña(dividendo , divisor , expected):
    assert disvision(dividendo,divisor) == expected