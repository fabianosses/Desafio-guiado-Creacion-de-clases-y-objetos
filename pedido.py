from te import Te

sabor = int(input("""
    Elige el sabor de té:
      1. Té negro.
      2. Té verde.
      3. Agua de hierbas
      """))

formato = int(input("Elige el formato (300 gr. ó 500 gr.): "))

nombre, tiempo, recomendacion = Te.tiempo_preparacion(sabor)

precio = Te.precio(formato)
print(precio)
print(f"""
    a. Sabor del tipo de té {nombre}
    b. Formato {formato}
    c. Precio {precio}
    d. Tiempo {tiempo}
    e. Recomendación {recomendacion}
      """)



