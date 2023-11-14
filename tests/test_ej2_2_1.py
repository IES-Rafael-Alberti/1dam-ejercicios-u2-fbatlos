import pytest
from src.ej2_2_1 import repetir_palabra

@pytest.mark.parametrize(
"palabra , expected",
[
    ("palabra" , "palabrapalabrapalabrapalabrapalabrapalabrapalabrapalabrapalabrapalabra"),
    ("no" , "nononononononononono"),
    ("ratón" , "ratónratónratónratónratónratónratónratónratónratón"), 
     ("mario" , "mariomariomariomariomariomariomariomariomariomario"),
    ("movil" , "movilmovilmovilmovilmovilmovilmovilmovilmovilmovil")
])

def test_palabra(palabra , expected):
    assert repetir_palabra(palabra) == expected