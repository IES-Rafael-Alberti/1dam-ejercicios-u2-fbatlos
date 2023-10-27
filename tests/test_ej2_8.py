import pytest
from src.ej2_8 import puntuacion

@pytest.mark.parametrize(
"puntos , expected",
[
    (0.4 , "Tu nivel de rendimiento es aceptable y tu dinero es 960.0 "),
    (0.0 , "Tu nivel de rendimiento es inaceptable y tu dinero es 0.0 "),
    (0.6 , "Tu nivel de rendimiento es meritorio y tu dinero es 1440.0 "), 
     (1 , "Tu nivel de rendimiento es meritorio y tu dinero es 2400 "),
    (0.2 , "ERROR")
])
def test_puntuacion(puntos , expected):
    assert puntuacion(puntos) == expected