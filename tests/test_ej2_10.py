import pytest
from src.ej2_10 import pizza

@pytest.mark.parametrize(
"vegano , ingrediente , expected",
[
    ("Si" , "1" , "La pizza es vegetariana y lleva tomate , mozzarella y pimiento"),
    ("no" , "2" , "La pizza es no vegetariana y lleva tomate , mozzarella y jamón"),
    ("NO" , "3" , "La pizza es no vegetariana y lleva tomate , mozzarella y salmón"), 
     ("sí" , "la otra" , "La pizza es vegetariana y lleva tomate , mozzarella y tofu"),
    ("No" , "1" , "La pizza es no vegetariana y lleva tomate , mozzarella y peperoni")
])

def test_pizza(vegano , ingrediente , expected):
    assert pizza(vegano , ingrediente) == expected