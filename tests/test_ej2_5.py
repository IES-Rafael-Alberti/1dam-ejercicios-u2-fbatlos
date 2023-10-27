import pytest
from src.ej2_5 import tributar

@pytest.mark.parametrize(
"edad ,ingresos , expected",
[
    (1 , 2 , "No tributas crack"),
    (10 , 27300 , "No tributas crack"),
    (50 , 3000 , "Tributas crack"),
    (20, 1 , "No tributas crack"), 
    (63 , 5000, "Tributas crack")
])
def test_tributar(edad , ingresos , expected):
    assert tributar(edad , ingresos) == expected