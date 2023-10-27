def grupos(nombre , sexo):
    nombre = nombre.upper()
    if (sexo == "F" and nombre < "M") or (sexo == "M" and nombre > "N"):
        return "Grupo A"
    else:
        return "Grupo B"
  
