import pytest
from src.ej2_9 import entrada

@pytest.mark.parametrize(
"edad , expected",
[
    (3 , "Pasas gratis"),
    (17 , "La entrada son 5€"),
    (23 , "La entrada son 10€"), 
     (1 , "Pasas gratis"),
    (18 , "La entrada son 10€")
])
def test_entrada(edad , expected):
    assert entrada(edad) == expected