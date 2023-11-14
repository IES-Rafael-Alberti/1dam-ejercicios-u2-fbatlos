import pytest
from src.ej2_1 import compara

@pytest.mark.parametrize(
"edad , expected",
[
    (1,"Eres menor de edad"),
    (16,"Eres menor de edad"),
    (17,"Eres menor de edad"),
    (52,"Eres mayor de edad"), 
    (19,"Eres mayor de edad")
])
def test_compara(edad, expected):
    assert compara(edad) == expected