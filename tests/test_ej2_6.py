import pytest
from src.ej2_6 import grupos

@pytest.mark.parametrize(
"nombre , sexo , expected",
[
    ("oscar" , "M" , "Grupo A"),
    ("julia" , "F" , "Grupo A"),
    ("ramona", "F" , "Grupo B"), 
     ("lorena" , "F" , "Grupo A"),
    ("miguel" , "M" , "Grupo B")
])
def test_grupos(nombre , sexo , expected):
    assert grupos(nombre , sexo) == expected