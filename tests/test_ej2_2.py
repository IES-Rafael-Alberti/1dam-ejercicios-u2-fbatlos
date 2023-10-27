import pytest
from src.ej2_2 import contraseña

@pytest.mark.parametrize(
"contraseña_introducida , expected",
[
    ("panconpan123","La contraseña es correcta"),
    ("panconpalta123","La contraseña es incorrecta"),
    ("panpan123","La contraseña es incorrecta"),
    ("panconpan124","La contraseña es incorrecta"), 
    ("PanConPan123","La contraseña es correcta")
])
def test_contraseña(contraseña_introducida, expected):
    assert contraseña(contraseña_introducida) == expected