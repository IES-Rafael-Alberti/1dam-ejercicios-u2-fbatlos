
def contraseña(contraseña_introducida):
    contraseña_guardada="panconpan123"
    contraseña_introducida=contraseña_introducida.lower()
    if contraseña_introducida == contraseña_guardada:
        return "La contraseña es correcta"
    else:
        return "La contraseña es incorrecta"